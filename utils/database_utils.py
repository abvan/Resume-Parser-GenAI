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

##Function that will save the parsing result in a table in the database.
def InsertParsingResults(result):
    # Create a new record
    parsing_result = ResumeMatchResult(
        candidate_name=result['candidate_name'],
        experience_in_years= '4.0',
        job_id=result['job_id'],
        match_percent=result['match_percent'],
        top_skills = str(', '.join(result['top_skills'])),
        verdict=result['Verdict'],
        reviewed_by= f"Model__{result['model_name']}",
        additional_comment=result['comments'],
        review_datetime=datetime.now(),  # Optional, as server_default will handle this if omitted
        resume_file_path=result['resume_file_path']
    )
    with current_app.app_context():
        db.create_all()
        db.session.add(parsing_result)
        db.session.commit()  
    print("record inserted")

def RetrieveParsingResults(job_id):
    with current_app.app_context():
        results = ResumeMatchResult.query.filter_by(job_id=job_id).order_by(desc(ResumeMatchResult.match_percent)).all()
    
    records = []
    for row in results:
        record = {column.name: getattr(row, column.name) for column in ResumeMatchResult.__table__.columns}
        records.append(record)
    return records
