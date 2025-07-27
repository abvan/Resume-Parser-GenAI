from models.ATS_models import *
from datetime import datetime
from flask import current_app


#Temporary Function for Testing
def insertsomething():
    jobHist = ResumeParsingHistory(63423,datetime.now())
    with current_app.app_context():
        db.create_all()
        db.session.add(jobHist)
        db.session.commit()
        all_students = Student.query.filter_by(fname='Vance').first().lname
        jobHist = ResumeParsingHistory.query.filter_by(job_id='63423').first().last_parse
        print(all_students)
        print(jobHist)

##Write a Function that will save the parsing result in a table in the database
##Input Pandas DataFrame or Json