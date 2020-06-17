import shutil
import psutil
import socket
import emails


def check_cpu_usage():
    """Returns True if the cpu is having too much usage, False otherwise"""
    max_cpu = 80

    if psutil.cpu_percent(1) > max_cpu:

        return "Error - CPU usage is over {}%".format(max_cpu)


def check_disk_space():
    """Returns True if there isn't enough disk space, False otherwise."""
    disk = "C:"
    min_percent_free = 20
    available_disk_space = shutil.disk_usage(disk)

    percent_free = 100 * available_disk_space.free / available_disk_space.total

    if percent_free < min_percent_free:
        
        return "Error - Availabe disk space is less than {}%".format(min_percent_free)


def check_available_memory():

    memory_usage = psutil.virtual_memory()
    #convert available memory from bytes to megabytes
    available_memory = memory_usage[1] / 2**20
    min_available_memory = 500
    
    if available_memory < min_available_memory:
       
        return "Error - Available memory is less than {}MB".format(min_available_memory) 


def check_hostname():

    domain_name = "localhost"
    hostname = socket.gethostbyname(domain_name)
    expected_address = "127.0.0."

    if hostname != expected_address:
       
        return "Error - {} cannot be resolved to {}".format(domain_name, expected_address)



def run_all_checks():

    health_checks = [
        (check_cpu_usage),
        (check_disk_space),
        (check_available_memory),
        (check_hostname)
        
    ]

    #configure email settings to send the error report
    sender = "localhost"
    recipient = "example@example.com"
    
    body = "Please check your system and resolve the issue as soon as possible."


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


