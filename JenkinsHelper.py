import shutil
import os
import jenkins


def print_free_disk_space():
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {total // (2**30)} GiB")
    print(f"Used: {used // (2**30)} GiB")
    print(f"Free: {free // (2**30)} GiB")


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
        
def move_text(self, source_file, destination_file):
    workspace = os.getcwd()
    source_path = os.path.join(workspace, source_file)
    destination_path = os.path.join(workspace, destination_file)

    try:
        with open(source_path, 'r') as source:
            content = source.read()
        with open(destination_path, 'w') as destination:
            destination.write(content)
        print(f"Text moved from '{source_path}' to '{destination_path}'.")
    except FileNotFoundError:
        print(f"File '{source_path}' does not exist.")
    except Exception as e:
        print(f"Error moving text from '{source_path}' to '{destination_path}': {e}")
        
def schedule_job(self, job_name, cron_expression):
    try:
        self.server.enable_job(job_name)
        self.server.quiet_period(job_name, 0)
        self.server.poll(job_name)
        self.server.build_job(job_name)
        print(f"Job '{job_name}' scheduled successfully with cron expression '{cron_expression}'.")
    except jenkins.JenkinsException as e:
        print(f"Failed to schedule job '{job_name}': {e}")
    except Exception as e:
        print(f"Unexpected error scheduling job '{job_name}': {e}")
