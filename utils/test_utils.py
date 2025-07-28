import os
import fitz  # PyMuPDF
import docx

#filepath = 'C:\\Users\Abhishek\\PROJECTS\\Resume_Parser_GenAI\\uploads\\resumes\\JobID-564\\AbhishekChavan_Resume_2025_20250727.pdf'
filepath = 'C:\\Users\\Abhishek\\Downloads\\Azure_Data_Engineer_JD.pdf'

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

print(extract_text(filepath))