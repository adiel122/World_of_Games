import jenkins
from jenkins import NotFoundException

# Define Jenkins server details
jenkins_url = 'http://localhost:8080'
username = 'admin'
password_or_api_token = '11e7a9c3c81256b5fee661f3d9d66b4e2f'

# Connect to Jenkins server
server = jenkins.Jenkins(jenkins_url, username=username, password=password_or_api_token)

# Create a new job
job_name = 'example-job'
job_config = """
<project>
  <actions/>
  <description>Example Job created using python-jenkins</description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.scm.NullSCM"/>
  <builders>
    <hudson.tasks.Shell>
      <command>echo Hello, Jenkins!</command>
    </hudson.tasks.Shell>
  </builders>
  <publishers/>
  <buildWrappers/>
</project>
"""

try:
    # Check if the job already exists
    job_info = server.get_job_info(job_name)
    print(f"Job '{job_name}' already exists. Not creating it again.")
except NotFoundException:
    # Job does not exist, so create it
    server.create_job(job_name, job_config)
    print(f"Job '{job_name}' created successfully.")
    
    
# Build the job
server.build_job(job_name)

# # Get the last build number
# last_build_number = server.get_job_info(job_name)['lastBuild']['number']
# 
# # Get the build info
# build_info = server.get_build_info(job_name, last_build_number)
# 
# print(f"Build Number: {build_info['number']}")
# print(f"Build Status: {build_info['result']}")
