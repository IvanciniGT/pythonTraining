from models.script_information import ScriptInformation
import sys

def we_have_an_error(message, user_data, error_code):
    print(message, file=sys.stderr)
    print("You provided: ", user_data, file=sys.stderr)
    sys.exit(error_code)

def validate_services(information : ScriptInformation):
    # It should be a list of dictionaries
            # isinstance... PYTHON BUILT-IN FUNCTION
            # It returns whether the object is an instance of the supplied class
    if not isinstance(information.services_information, list):
        we_have_an_error("The services information should be a list of services.", information.services_information, 5)
    for service in information.services_information:
        validate_service(service)

def validate_service(service):
    # Each dictionary should have the following keys:
    # - address
    # - port
    # - protocol    
    if not isinstance(service, dict):
        we_have_an_error("Each service should be a dictionary.", service, 6)
    if 'address' not in service:
        we_have_an_error("Each service should have an address key.", service, 7)
    if 'port' not in service:
        we_have_an_error("Each service should have a port key.", service, 8)
    else:
        # Port should contain a valid value
        if(service['port'] < 0 or service['port'] > 65536):
            we_have_an_error("The port should be a number between 1 and 65535.", service['port'], 10)
    if 'protocol' not in service:
        we_have_an_error("Each service should have a protocol key.", service, 9)

def validate_parallel_tasks(information : ScriptInformation):
    # We also need to validate that the parallel tasks is a number
    # and that it is greater than 0
    try:
        if(int(information.parallel_tasks) > 0):
            return # break the function
    except ValueError:
        pass
    we_have_an_error("The number of parallel tasks should be a number.", information.parallel_tasks, 4)

def validate_my_script_information(information : ScriptInformation):
    validate_services(information)
    validate_parallel_tasks(information)
