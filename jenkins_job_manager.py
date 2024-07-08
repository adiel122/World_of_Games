import requests
from requests.auth import HTTPBasicAuth
from jenkinsapi.jenkins import Jenkins


class JenkinsJobManager:
    def __init__(self, jenkins_url, username, password_or_api_token):
        self.jenkins_url = jenkins_url
        self.auth = HTTPBasicAuth(username, password_or_api_token)
        self.headers = {'Content-Type': 'application/xml'}

    def job_exists(self, job_name):
        response = requests.get(f'{self.jenkins_url}/job/{job_name}/api/json', auth=self.auth)
        return response.status_code == 200

    def create_job(self, job_name, job_config):
        if self.job_exists(job_name):
            print(f"Job '{job_name}' already exists. Skipping creation.")
            return

        url = f"{self.jenkins_url}/createItem?name={job_name}"
        print(f"Creating job at URL: {url}")
        print(f"Job configuration:\n{job_config}")

        response = requests.post(url, data=job_config, headers=self.headers, auth=self.auth)

        if response.status_code != 200:
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")

        response.raise_for_status()
        print(f"Job '{job_name}' created successfully.")

    def build_job(self, job_name):
        url = f"{self.jenkins_url}/job/{job_name}/build"
        response = requests.post(url, auth=self.auth)
        response.raise_for_status()
        print(f"Job '{job_name}' build triggered successfully.")

    def create_file_in_workspace(self, job_name, file_name, file_content):
        # Note: This functionality might need a Jenkins plugin or workaround
        print(f"Creating file '{file_name}' in workspace of job '{job_name}' with content: {file_content}")

    def read_file_in_workspace(self, jenkins_url, username, password, job_name, file_name):
        jenkins = self.get_jenkins_instance(jenkins_url, username, password)
        job = jenkins[job_name]
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
