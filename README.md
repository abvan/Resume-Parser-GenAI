# 🧠 Resume-Parser-GenAI

### Automate Resume Parsing & Candidate Selection using Generative AI

This project leverages Generative AI (GenAI) to automate resume parsing and intelligent candidate shortlisting for job postings. It simplifies and accelerates the recruitment pipeline by extracting structured data from resumes and identifying top-matching candidates based on the job description, extracted and inferred skills, and contextual fit.

---

## 🚀 Features

- 📄 **Resume Parsing**: Automatically extracts structured information such as name, email, phone number, skills, education, and work experience from resumes (PDF/DOCX).
- 🔍 **Job Matching Engine**: Matches candidate profiles with job descriptions using semantic similarity and contextual analysis.
- 🤖 **GenAI-based Skill Inference**: Uses Large Language Models (LLMs) like GPT-4 to infer implicit or missing skills from resumes based on job context.
- 📊 **Ranking & Recommendation**: Generates a match score, provides verdicts (Shortlist/Hold/Reject), and ranks candidates accordingly.
- 🧰 **Web UI (Optional)**: A simple Flask-based interface for uploading resumes, selecting a job description, and viewing results.

---

## 🛠️ Tech Stack

| Layer           | Technologies                                                                  |
|----------------|--------------------------------------------------------------------------------|
| **Backend**     | Python, Flask                                                                 |
| **AI & NLP**    | LangChain, Groq, OpenAI GPT-4 / LLaMA (Optional),spaCy(TBD), Gensim(TBD), NLTK(TBD)     |
| **Vector DB**   | FAISS / ChromaDB (Optional for semantic search or embeddings storage) (TBD)   |
| **Frontend**    | HTML, CSS, JavaScript                                                         |
| **Utilities**   | Pandas, Scikit-learn, Python-dotenv,PyMuPDF, pdfplumber, docx2txt             |

---

## 📂 Folder Structure



---

## ✅ How It Works

1. **Upload Resumes**  
   Users upload resumes in PDF or DOCX format via the UI.

2. **Parse & Extract Info**  
    Parsers extract the text from the resumes

4. **Job Description Matching**  
   Job description is analyzed and compared with parsed resumes using embeddings(TBD) and LLM prompts.

5. **Scoring & Verdict**  
   Each candidate is scored and categorized as *Shortlist*, *Hold*, or *Reject* based on their fit.

6. **Results Displayed**  
   Results can be displayed in the web UI or exported to CSV/Excel.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Resume-Parser-GenAI.git
cd Resume-Parser-GenAI
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the `config/` folder:

```env
GROQ_API_KEY = your_groq_key_here
```

### 4. Run the Application

```bash
python app/main.py
```

or using the shell script:

```bash
bash run.sh
```

---

## 📈 Example Output

| Candidate Name | Match % | Verdict   | Suitable Role       | Comments                            |
|----------------|---------|-----------|----------------------|-------------------------------------|
| John Doe       | 88.7    | Shortlist | Azure Data Engineer | Strong ADF and Databricks exposure |
| Priya Sharma   | 72.3    | Hold      | Data Analyst         | Lacks cloud experience              |
| Rohit Mehta    | 95.1    | Shortlist | ML Engineer          | Excellent match, NLP experience     |

---

## 📌 TODO / Enhancements

- [ ] LLMs infererencing additional skills that are not explicitly mentioned but are implied from job roles or past experience.
- [ ] Add More NLP/Embedding Techniques to extract only releveant text which would improve the efficiency and Accuracy of the tool.
- [ ] Add support for LinkedIn profile parsing
- [ ] Enable admin dashboard to manage job openings
- [ ] Integrate with ATS systems
- [ ] Add support for multiple LLM providers (Anthropic, Cohere)
- [ ] Improve PDF parsing accuracy using OCR fallback

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---
