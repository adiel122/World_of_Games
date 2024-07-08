import time
import argparse
import os
from jenkins_job_manager import JenkinsJobManager
from jenkins_job_config import JenkinsJobConfig, JenkinsJobReader
from JenkinsHelper import print_free_disk_space

print("Adiel is the best!")

jenkins_url = 'http://localhost:8080'
username = 'admin'
password_or_api_token = '111e6b82a7320b8ec2c88401592594c337'


job_name = os.environ.get('JobName')

if not job_name:
    raise EnvironmentError("The environment variable 'JobName' is not set.")

# Get job configuration using JenkinsJobConfig and JenkinsJobReader
job_config = JenkinsJobConfig().get_config()
reader = JenkinsJobReader(job_config)
job_details = reader.read_config()

jenkins_manager = JenkinsJobManager(jenkins_url, username, password_or_api_token)

jenkins_manager.create_job(job_name, job_config)
time.sleep(10)
jenkins_manager.build_job(job_name)

if job_name == 'create_file':
    

elif job_name == 'read_file':
    

elif job_name == 'free_disk':
    print_free_disk_space()

elif job_name == 'move_text':
    # Implement the logic for move_text
    pass

elif job_name == 'schedule':
    # Implement the logic for schedule
    pass

else:
    print("Invalid action.")

# Print job details
print("SCM URL:", job_details['scm_url'])
print("Branch Name:", job_details['branch_name'])
print("Build Command:", job_details['build_command'])
