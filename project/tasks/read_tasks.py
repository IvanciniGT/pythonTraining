import sys
import os
import yaml
from models.script_information import ScriptInformation

ENVIRONMENT_VARIABLE_NAME           = 'CHECK_SERVICES_PARALLEL_TASKS_COUNT'
DEFAULT_NUMBER_OF_PARALLEL_TASKS    = 2
INVALID_ARGUMENTS_MESSAGE           = """
Invalid script usage.
Usage: python3 checkService.py <services_file_name>

Where: <services_file_name> is the name of the YAML file containing the services information.
"""

def read_all_the_script_information():
    file_name               = read_the_file_name()
    environment_variables   = read_some_environment_variables()
    services_information    = read_the_services_information_file(file_name)
    return ScriptInformation(file_name, environment_variables, services_information)

def read_the_file_name():
    # The user will supply that information (file name) as the first argument of the script
    # $ python3 checkService.py services.yaml
    # sys.argv = ['checkService.py', 'services.yaml']
    # In order to be able to read arguments of the script, we need to import the sys module
    # The sys module has a list called argv which contains all the arguments passed to the script
    if(len(sys.argv) != 2):
        # By default, the print function will print the message to the standard output.
        # As this is an error message, we should print it to the standard error output.
        # We can access that error output using the sys module, and supplying the file=sys.stderr argument
        print(INVALID_ARGUMENTS_MESSAGE, file=sys.stderr)
        exit(1) # Stop the script execution... And return an error code: 1
    return sys.argv[1]

def read_some_environment_variables():
    # We already know how to do it.. by using the os module
    max_tasks = os.getenv(ENVIRONMENT_VARIABLE_NAME, DEFAULT_NUMBER_OF_PARALLEL_TASKS)
    return {
        "parallel_tasks": max_tasks
    }

def read_the_services_information_file(file_name):
    # Check if the file exists
    if not os.path.exists(file_name):
        print("The provided services information file does not exist: "+ file_name, file=sys.stderr)
        exit(2)
    with open(file_name, "r") as my_file_channel:
        try:
            return yaml.load(my_file_channel, Loader=yaml.SafeLoader)
        except Exception as e:
            print("Invalid services information file: "+ file_name, file=sys.stderr)
            print(e, file=sys.stderr)
            exit(3)
