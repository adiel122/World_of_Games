import shutil
import os
import jenkins
import xml.etree.ElementTree as ET

from JenkinsMain import jenkins_url, username, password_or_api_token
from jenkins_job_manager import JenkinsJobManager

jenkins_manager = JenkinsJobManager(jenkins_url, username, password_or_api_token)


def print_free_disk_space():
    total, used, free = shutil.disk_usage("/")
    print(f"Total: {total // (2 ** 30)} GiB")
    print(f"Used: {used // (2 ** 30)} GiB")
    print(f"Free: {free // (2 ** 30)} GiB")


def create_file_in_workspace(file_name, content):
    workspace = os.getcwd()
    full_path = os.path.join(workspace, file_name)

    try:
        with open(full_path, 'w') as file:
            file.write(content)
        print(f"File '{full_path}' created successfully.")
    except Exception as e:
        print(f"Error creating file '{full_path}': {e}")


def read_file_in_workspace(file_name):
    workspace = os.getcwd()
    full_path = os.path.join(workspace, file_name)

    # Read and print the file content
    try:
        with open(full_path, 'r') as file:
            content = file.read()
        print(f"Content of '{full_path}':\n{content}")
    except FileNotFoundError:
        print(f"File '{full_path}' does not exist.")


def move_text(source_file, destination_file):
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


def schedule_job(job_name, new_cron_expression):
    try:
        # Create a Jenkins server instance
        server = jenkins.Jenkins(jenkins_url, username=username, password=password_or_api_token)

        # Get the current job configuration XML
        config_xml = server.get_job_config(job_name)

        # Parse the XML
        root = ET.fromstring(config_xml)

        # Find the <triggers> element
        triggers = root.find('triggers')
        if triggers is None:
            # If no <triggers> element, create one
            triggers = ET.SubElement(root, 'triggers', {'class': 'vector'})

        # Remove existing cron triggers
        for trigger in triggers.findall('hudson.triggers.TimerTrigger'):
            triggers.remove(trigger)

        # Add the new cron trigger
        timer_trigger = ET.SubElement(triggers, 'hudson.triggers.TimerTrigger')
        spec = ET.SubElement(timer_trigger, 'spec')
        spec.text = new_cron_expression

        # Convert the modified XML back to a string
        new_config_xml = ET.tostring(root, encoding='unicode')

        # Update the job with the new configuration
        server.reconfig_job(job_name, new_config_xml)

        print(f"Job '{job_name}' schedule updated successfully to '{new_cron_expression}'.")
    except jenkins.JenkinsException as e:
        print(f"Failed to update job '{job_name}': {e}")
    except Exception as e:
        print(f"Unexpected error updating job '{job_name}': {e}")
