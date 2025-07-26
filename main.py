import os
import uuid
from datetime import datetime,date
from flask import Flask, request, render_template, jsonify, flash, redirect, url_for,render_template_string
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from models.ATS_models import *
from dotenv import load_dotenv
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

#Temporary Function for Testing
def insertsomething():
    jobHist = ResumeParsingHistory(5432,datetime.now())
    with app.app_context():
        db.create_all()
        db.session.add(jobHist)
        db.session.commit()
        all_students = Student.query.filter_by(fname='Vance').first().lname
        jobHist = ResumeParsingHistory.query.filter_by(job_id='5432').first().last_parse
        print(all_students)
        print(jobHist)

#Generate a unique filename to avoid conflicts
def generate_unique_filename(filename):
    name, ext = os.path.splitext(secure_filename(filename))
    timestamp = date.today().strftime('%Y%m%d')
    unique_id = str(uuid.uuid4())[:8]
    return f"{name}_{timestamp}{ext}"

#Create folder for a new jobid if not exists
def create_folder_path(job_id):
    folder_name = f"JobID-{job_id}"
    folder_path = os.path.join(app.config['UPLOAD_PATH'],folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Folder '{folder_path}' created.")
    else :
        print(f"Folder '{folder_path}' already exists.")
    return folder_path


@app.route('/', methods=['GET', 'POST'])
def index():
    insertsomething()

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
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':  
    app.run(debug=True) 