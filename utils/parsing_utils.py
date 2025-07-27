from flask import current_app


## Write a Funtion that will scan all the files in the folder for the required job_id and return the results in pandas dataframe or JSON
## Input : job-id, Job Description.
## Functionality : Search for the folder of the job-id , traverse all the resumes in the folder and compare it with the JD using LLM.
## Output : Pandas DF, JSON.