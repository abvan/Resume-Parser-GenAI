from flask import current_app
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os
import json
import os
import fitz  # PyMuPDF
import docx
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

## Write a Funtion that will scan all the files in the folder for the required job_id and return the results in pandas dataframe or JSON
## Input : job-id, Job Description.
## Functionality : Search for the folder of the job-id , traverse all the resumes in the folder and compare it with the JD using LLM.
## Output : Pandas DF, JSON.

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if (ext == '.pdf') :
            doc = fitz.open(file_path)
            return "\n".join([page.get_text() for page in doc])
    elif (ext == '.docx') :
            doc = docx.Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file type: " + ext)

def parser(jd_text,resume_text):
    
    # Initialize the Groq LLM
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama3-70b-8192",
        temperature=0.0,
        top_p=1.0
    )
    
    # Create the prompt template
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are an expert HR analyst. Always return a JSON response with exact keys: match_percent, status, top_skills. 
        Be consistent and deterministic in your analysis.
        
        Rules for status decision:
        - Reject: <40% match
        - Hold: 40-65% match  
        - Shortlist: >65% match"""),
        ("user", """Job Description Text: {jd_text} Resume Text:{resume_text}

        Compare the Job description and the Resume :
        - Return a match percentage based on overlap
        - Decide if the resume should be 'Shortlist', 'Hold', or 'Reject'
        - List the top 5 most relevant skills (no suggestions or explanations)

        Return a JSON with keys: match_percent, status, top_skills.""")
    ])

    # Create the output parser
    parser = JsonOutputParser()

    # Create the chain
    chain = prompt_template | llm | parser

  
    try:
        # Execute the chain
        result = chain.invoke({
            "jd_text": jd_text,
            "resume_text": resume_text
        })
        return result    
    except Exception as e:
        print("LangChain Processing Error:", e)
        # Fallback response
        return {
            "match_percent": 0,
            "status": "Reject",
            "top_skills": []
        }
    
# filepath= 'C:\\Users\\Abhishek\\Downloads\\Azure_Data_Engineer_JD.pdf'
# jd_text = extract_text(filepath)
# filepath = 'C:\\Users\Abhishek\\PROJECTS\\Resume_Parser_GenAI\\uploads\\resumes\\JobID-564\\AbhishekChavan_Resume_2025_20250727.pdf'
# resume_text = extract_text(filepath)
# result = parser(jd_text,resume_text)

# print(result)