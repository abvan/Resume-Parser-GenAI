import os
import uuid
import logging
from datetime import datetime,timedelta
from werkzeug.utils import secure_filename
from flask import current_app


#Generate a unique filename to avoid conflicts
def generate_unique_filename(filename):
    name, ext = os.path.splitext(secure_filename(filename))
    timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
    unique_id = str(uuid.uuid4())[:8]
    return f"{name}_{timestamp}{ext}"

#Create folder for a new jobid if not exists
def create_folder_path(job_id):
    folder_name = f"JobID-{job_id}"
    folder_path = os.path.join(current_app.config['UPLOAD_PATH'],folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Folder '{folder_path}' created.")
    else :
        print(f"Folder '{folder_path}' already exists.")
    return folder_path

#Get the List of Resumes that were uploaded in last 1 Min
def get_latest_upload(job_id):
    latest_files = []
    folder_path = os.path.join(current_app.config['UPLOAD_PATH'],f"JobID-{job_id}")
    if not os.path.exists(folder_path):
        latest_files.append('Folder Does Not Exists')
        return latest_files
    
    time_threshold = datetime.now() - timedelta(minutes=1) # 1-minute window
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            # Check if modified time is within the last 1 minute
            if modified_time >= time_threshold:
                latest_files.append(filename)

    return latest_files

#Get the JobDescription based on the JobID
def get_jd_filepath(job_id):
    print(job_id)
    pass