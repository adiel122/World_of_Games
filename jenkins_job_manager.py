from jenkinsapi.jenkins import Jenkins
import time

class JenkinsJobManager:
    def __init__(self, url=None, username=None, password=None):
        self.jenkins = None
        if url and username and password:
            self.jenkins = Jenkins(url, username=username, password=password)

    def get_jenkins_instance(self, url, username, password):
        return Jenkins(url, username=username, password=password)

    def create_job(self, job_name, job_config):
        if not self.jenkins:
            raise ValueError("Jenkins instance is not initialized.")
        if job_name in self.jenkins.jobs:
            print(f"Job '{job_name}' already exists.")
        else:
            self.jenkins.create_job(job_name, job_config)
            print(f"Job '{job_name}' created successfully.")

    def build_job(self, job_name):
        if not self.jenkins:
            raise ValueError("Jenkins instance is not initialized.")
        job = self.jenkins[job_name]
        job.invoke(build_params=None)
        print(f"Job '{job_name}' build triggered.")

    def create_file_in_workspace(self, job_name, file_name, content):
        if not self.jenkins:
            raise ValueError("Jenkins instance is not initialized.")
        job = self.jenkins[job_name]
        build = job.get_last_build()
        workspace = build.get_workspace()
        file_path = f"{workspace}/{file_name}"
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{file_name}' created in workspace of job '{job_name}'.")

    def read_file_in_workspace(self, job_name, file_name):
        if not self.jenkins:
            raise ValueError("Jenkins instance is not initialized.")
        job = self.jenkins[job_name]
        build = job.get_last_build()
        workspace = build.get_workspace()

        file_path = f"{workspace}/{file_name}"
        print(f"Reading file '{file_name}' in workspace of job '{job_name}'")

        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)
        except Exception as e:
            print(f"Error reading file: {e}")
