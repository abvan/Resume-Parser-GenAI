import os
import uuid
from datetime import datetime,date
from flask import Flask, request, render_template, jsonify, flash, redirect, url_for,render_template_string
from werkzeug.utils import secure_filename
#from werkzeug.exceptions import RequestEntityTooLarge

app = Flask(__name__)
#app.secret_key = 'your-secret-key-change-this'  # Change this to a secure secret key 


app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'docx'}
app.config['UPLOAD_PATH'] = 'uploads/resumes/'


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