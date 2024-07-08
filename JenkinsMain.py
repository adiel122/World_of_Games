import time
from jenkins_job_manager import JenkinsJobManager
from jenkins_job_config import JenkinsJobConfig, JenkinsJobReader

jenkins_url = 'http://localhost:8080'
username = 'admin'
password_or_api_token = '11e7a9c3c81256b5fee661f3d9d66b4e2f'

file_name = 'example.txt'
job_name = 'Github_Job'

# Get job configuration using JenkinsJobConfig and JenkinsJobReader
job_config = JenkinsJobConfig().get_config()
reader = JenkinsJobReader(job_config)
job_details = reader.read_config()

jenkins_manager = JenkinsJobManager(jenkins_url, username, password_or_api_token)
jenkins_manager.create_job(job_name, job_config)

# Add a delay to ensure the job is properly registered before triggering a build
time.sleep(10)

jenkins_manager.build_job(job_name)
jenkins_manager.create_file_in_workspace(job_name, file_name, 'This file is created during the build job.')

jenkins_manager.read_file_in_workspace(job_name, file_name)

# Print job details
print("SCM URL:", job_details['scm_url'])
print("Branch Name:", job_details['branch_name'])
print("Build Command:", job_details['build_command'])