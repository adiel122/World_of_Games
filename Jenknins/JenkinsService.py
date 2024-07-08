from jenkins import  JenkinsException
import time
import os

def create_job(self, job_name, job_config):
    if self.job_exists(job_name):
        print(f"Job '{job_name}' already exists. Not creating it again.")
    else:
        try:
            self.server.create_job(job_name, job_config)
            print(f"Job '{job_name}' created successfully.")
            # Wait and check if the job is created
            for _ in range(5):
                if self.job_exists(job_name):
                    print(f"Job '{job_name}' now exists.")
                    break
                time.sleep(2)
            else:
                print(f"Job '{job_name}' does not exist after creation attempt.")
        except JenkinsException as e:
            print(f"JenkinsException when creating job '{job_name}': {e}")
        except Exception as e:
            print(f"Unexpected error when creating job '{job_name}': {e}")

def build_job(self, job_name):
    if self.job_exists(job_name):
        try:
            self.server.build_job(job_name)
            print(f"Job '{job_name}' build triggered successfully.")
        except JenkinsException as e:
            print(f"Failed to trigger build for job '{job_name}': {e}")
        except Exception as e:
            print(f"Unexpected error triggering build for job '{job_name}': {e}")
    else:
        print(f"Job '{job_name}' does not exist. Cannot trigger build.")

def create_file_in_workspace(self, file_name, content):
    workspace = os.getcwd()
    full_path = os.path.join(workspace, file_name)

    try:
        with open(full_path, 'w') as file:
            file.write(content)
        print(f"File '{full_path}' created successfully.")
    except Exception as e:
        print(f"Error creating file '{full_path}': {e}")

def read_file_in_workspace(self, file_name):
    workspace = os.getcwd()
    full_path = os.path.join(workspace, file_name)

    # Read and print the file content
    try:
        with open(full_path, 'r') as file:
            content = file.read()
        print(f"Content of '{full_path}':\n{content}")
    except FileNotFoundError:
        print(f"File '{full_path}' does not exist.")
        