import os
import uuid
import logging
from datetime import date
from werkzeug.utils import secure_filename
from flask import current_app


#Generate a unique filename to avoid conflicts
def generate_unique_filename(filename):
    name, ext = os.path.splitext(secure_filename(filename))
    timestamp = date.today().strftime('%Y%m%d')
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