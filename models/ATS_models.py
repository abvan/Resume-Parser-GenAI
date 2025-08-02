from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Numeric, Text, CheckConstraint,Enum, DateTime, func

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(40))
    lname =db.Column(db.String(40))
    pet = db.Column(db.String(40))

    def __init__(self,fname,lname,pet):
        self.fname = fname
        self.lname = lname
        self.pet = pet

class ResumeParsingHistory(db.Model):
    __tablename__ = 'Resume_Parsing_History'
    __table_args__ = {'schema': 'ats'}
    job_id = db.Column(db.Integer,primary_key=True)
    last_parse = db.Column(db.TIMESTAMP)

    def __init__(self,job_id,last_parse):
        self.job_id = job_id
        self.last_parse = last_parse

## Create a Table which will store all the parsing results
class ResumeMatchResult(db.Model):
    __tablename__ = 'resume_match_results'
    __table_args__ = (
            db.CheckConstraint('match_percent BETWEEN 0 AND 100', name='match_percent_range'),
            db.CheckConstraint("verdict IN ('Reject', 'Hold', 'Shortlist')", name='verdict_valid'),
            {'schema': 'ats'}  # Schema name
        )

    result_id = db.Column(Integer, primary_key=True, autoincrement=True)
    candidate_name = db.Column(String(100), nullable=False)
    job_id = db.Column(Integer, nullable=False)
    match_percent = db.Column(Numeric(5, 2))
    top_skills = db.Column(Text)
    verdict = db.Column(String(20))
    reviewed_by = db.Column(String(100))
    additional_comment = db.Column(Text)
    review_datetime = db.Column(DateTime, server_default=func.now())
    resume_file_path = db.Column(Text)
   
    
    def __init__(self,candidate_name,job_id,match_percent,verdict,additional_comment,reviewed_by,review_datetime,resume_file_path):
        self.candidate_name = candidate_name
        self.job_id = job_id
        self.match_percent = match_percent
        self.verdict = verdict
        self.reviewed_by = reviewed_by
        self.additional_comment = additional_comment
        self.review_datetime =review_datetime
        self.resume_file_path = resume_file_path
