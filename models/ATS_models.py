from flask_sqlalchemy import SQLAlchemy

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