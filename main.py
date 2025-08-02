import os
import uuid
from datetime import datetime,date
from flask import Flask, request, render_template, jsonify, flash, redirect, url_for,render_template_string
from werkzeug.utils import secure_filename
from models.ATS_models import *
from dotenv import load_dotenv
from utils.file_utils import *
from utils.database_utils import *
from utils.parsing_utils import *
#from werkzeug.exceptions import RequestEntityTooLarge

load_dotenv()
##Getting Credentials
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_SSLMODE = os.environ.get('DB_SSLMODE','prefer')

app = Flask(__name__)
#app.secret_key = 'your-secret-key-change-this'  # Change this to a secure secret key 


app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'docx'}
app.config['UPLOAD_PATH'] = 'uploads/resumes/'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_id = request.form['job_id']
        folder_path = create_folder_path(job_id)
        
        #Receive multiple files from the post request and saves it to the disk.
        for uploaded_file in request.files.getlist('resumes'):
            filename = secure_filename(uploaded_file.filename)
            if uploaded_file.filename != '':
                file_ext = filename.rsplit('.', 1)[1].lower()
                
                #Accepting only secureed File Extensions
                if file_ext not in app.config['ALLOWED_EXTENSIONS']:
                    return render_template_string("""<body>Not allowed<body>""") # TEMPORARY : CHANGE THIS
              
                unique_filename = generate_unique_filename(uploaded_file.filename)
                uploaded_file.save(os.path.join(folder_path, unique_filename))
        return redirect(url_for('parse_job_resumes',job_id=job_id))
    return render_template('index.html')

@app.route('/parse_resumes/<job_id>', methods=['GET', 'POST'])
def parse_job_resumes(job_id):
                    
    fileListToParse = get_latest_upload(job_id)
    #Get the JD Text- THINK SOMETHING ON JD PART
    filepath= 'C:\\Users\\Abhishek\\Downloads\\Azure_Data_Engineer_JD.pdf'
    jd_Text = extract_text(filepath)
    
    folder_name = f"JobID-{job_id}"
    for fileName in fileListToParse :
        print(fileName)
        filepath = os.path.join(current_app.config['UPLOAD_PATH'],folder_name,fileName).replace("\\", "/")
        resume_Text = extract_text(filepath)
        json_result = resume_parser(jd_Text,resume_Text) #Calling and Comparing Using LLM
#       json_result = {'match_percent': 83, 'Verdict': 'Shortlist', 'top_skills': ['Azure Data Factory', 'Azure Databricks', 'Azure DevOps', 'Python', 'Azure Synapse Analytics'], 'comments': 'The candidate has a strong background in Azure data engineering, with relevant experience in designing and building scalable data pipelines. The certifications in Azure Data Engineer and Fabric Data Engineer are a plus. However, the resume could benefit from more details on data governance and security aspects.'}  
        filenameparts = fileName.split('_')
        json_result['candidate_name'] = filenameparts[0] #+" "+filenameparts[1]
        json_result['job_id'] = job_id
        json_result['resume_file_path'] = filepath

    #4 Append the Result for all the resumes
    #5 Save it in a Database
    InsertParsingResults(json_result)
    #json_result = {'match_percent': 82, 'Verdict': 'Shortlist', 'top_skills': ['Azure Data Factory', 'Azure Databricks', 'Azure DevOps', 'Python', 'SQL'], 'comments': 'The candidate has a strong background in Azure data engineering, with relevant experience in designing and building scalable data pipelines. The certifications in Microsoft Azure and Databricks are a plus. However, the resume could be improved by highlighting more specific examples of data governance, security, and privacy regulations experience.'}
    
    #6 Display it in the FrontEnd (JobRelated)


    return render_template_string("""
        <H1>Hello PARSED RESUME</H1><body>
        <h2>Items in the List:</h2>
        <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
                                  """)

if __name__ == '__main__':  
    app.run(debug=True) 