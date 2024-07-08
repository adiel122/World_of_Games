import JenkinsHelper as helper
import os

file_name = 'example.txt'
source_file = '/path/to/source/'+file_name
destination_directory = '/path/to/destination/directory'

def run_job_details():
    job_name = os.environ.get('JOB_NAME')
    if job_name == 'create_file':
        helper.create_file_in_workspace(file_name,'This file is created during the build job.')
    elif job_name == 'read_file':
        helper.read_file_in_workspace(file_name)
    elif job_name == 'free_disk':
        helper.print_free_disk_space()
    elif job_name == 'move_text':
        helper.move_text(source_file,destination_directory)
    elif job_name == 'schedule':
        helper.schedule_job(job_name, "0 8 * * *")
    else:
        print("Invalid action.")
        
run_job_details()