from jenkins import  JenkinsException
import time

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
        