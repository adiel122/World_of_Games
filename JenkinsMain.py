import time
import os
from jenkins_job_manager import JenkinsJobManager
from jenkins_job_config import JenkinsJobConfig, JenkinsJobReader


print("Adiel is the best!")

jenkins_url = 'http://localhost:8080'
username = 'admin'
password_or_api_token = '111e6b82a7320b8ec2c88401592594c337'


job_name = os.environ.get('JobName')
print(job_name)

# Get job configuration using JenkinsJobConfig and JenkinsJobReader
job_config = JenkinsJobConfig().get_config()
reader = JenkinsJobReader(job_config)
job_details = reader.read_config()

jenkins_manager = JenkinsJobManager(jenkins_url, username, password_or_api_token)

def is_not_empty(value):
    return value is not None and value != ""

if is_not_empty(job_name) and is_not_empty(job_config):
    jenkins_manager.create_job(job_name, job_config)
    time.sleep(10)
    jenkins_manager.build_job(job_name)
else:
    print("Error: job_name and job_config must not be null or empty.")



# Print job details
print("SCM URL:", job_details['scm_url'])
print("Branch Name:", job_details['branch_name'])
print("Build Command:", job_details['build_command'])
