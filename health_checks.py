import shutil
import psutil
import socket
import emails


def check_cpu_usage():
    """Returns an alert if CPU usage goes over the specified max cpu amount"""
    max_cpu = 80

    if psutil.cpu_percent(1) > max_cpu:

        return f"Error - CPU usage is over {max_cpu}%"


def check_disk_space():
    """Returns an alert if the available space on the selected disk goes under the specified minimum."""
    disk = "C:"
    min_percent_free = 20
    available_disk_space = shutil.disk_usage(disk)

    percent_free = 100 * available_disk_space.free / available_disk_space.total

    if percent_free < min_percent_free:
        
        return f"Error - Availabe disk space is less than {min_percent_free}%"


def check_available_memory():
    """Returns an alert if the amount of available memory falls below the specified minimum"""
    memory_usage = psutil.virtual_memory()

    #convert available memory from bytes to megabytes
    available_memory = memory_usage[1] / 2**20
    min_available_memory = 1000
    
    if available_memory < min_available_memory:
       
        return f"Error - Available memory is less than {min_available_memory}MB"


def check_hostname():
    """Returns an alert if the specified hostname can't be resolved to the expected IP address"""
    domain_name = "localhost"
    hostname = socket.gethostbyname(domain_name)
    expected_address = "127.0.0.1"

    if hostname != expected_address:
       
        return f"Error - {domain_name} cannot be resolved to {expected_address}"



def run_all_checks():
    """Runs a series of health check functions and generates an email if there are any alerts"""

    #create a list of all the health check functions
    health_checks = [
        (check_cpu_usage),
        (check_disk_space),
        (check_available_memory),
        (check_hostname)
        
    ]

    #configure basic email settings to send the error report
    sender = "example@example.com"
    recipient = "example@example.com"    
    body = "System issues have been detected. Please check your system and resolve the issue as soon as possible."

    #iterate through all functions in the health_checks list and run each function. If the function returns an alert, send an email
    for check in health_checks:

        check_output = check()

        if check_output:

            #set the email subject to the error message of the check that failed
            subject = check_output       
            error_report_email = emails.generate_email(sender, recipient, subject, body)
            emails.send_email(error_report_email)
            

    if not check_output:
       print("All checks passed.")
        
    

if __name__ == "__main__":

    run_all_checks()


