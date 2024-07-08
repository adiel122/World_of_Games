import jenkins
from jenkins import NotFoundException

class JenkinsJobManager:
    import jenkins
from jenkins import NotFoundException
import os

class JenkinsJobManager:
    def __init__(self, jenkins_url, username, password_or_api_token):
        self.server = jenkins.Jenkins(jenkins_url, username=username, password=password_or_api_token)

    def job_exists(self, job_name):
        try:
            self.server.get_job_info(job_name)
            return True
        except NotFoundException:
            return False

    def create_job(self, job_name, job_config):
        if self.job_exists(job_name):
            print(f"Job '{job_name}' already exists. Not creating it again.")
        else:
            self.server.create_job(job_name, job_config)
            print(f"Job '{job_name}' created successfully.")

    def build_job(self, job_name):
        if self.job_exists(job_name):
            self.server.build_job(job_name)
            print(f"Job '{job_name}' build triggered successfully.")
            self.create_file_in_workspace('example.txt', 'This file is created during the build job.')
        else:
            print(f"Job '{job_name}' does not exist. Cannot trigger build.")

    def create_file_in_workspace(self, file_name, content):
        workspace = os.getcwd()
        full_path = os.path.join(workspace, file_name)

        with open(full_path, 'w') as file:
            file.write(content)

        print(f"File '{full_path}' created successfully.")

def main():
    jenkins_url = 'http://localhost:8080'
    username = 'admin'
    password_or_api_token = '11e7a9c3c81256b5fee661f3d9d66b4e2f'

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

    jenkins_manager = JenkinsJobManager(jenkins_url, username, password_or_api_token)
    jenkins_manager.create_job(job_name, job_config)
    jenkins_manager.build_job(job_name)
    jenkins_manager.create_file_in_workspace('example.txt', 'This file is created during the build job.')

if __name__ == "__main__":
    main()
