import os
import uuid
from datetime import datetime,date
from flask import Flask, request, render_template, jsonify, flash, redirect, url_for,render_template_string
from werkzeug.utils import secure_filename
from models.ATS_models import *
from dotenv import load_dotenv
from utils.file_utils import *
from utils.database_utils import *
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

@app.route('/parser', methods=['GET', 'POST'])
def parser():
    #insertsomething()

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