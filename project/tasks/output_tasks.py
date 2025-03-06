import jinja2
from models.result_information import ResultInformation
from models.script_information import ScriptInformation
import sys
import json

CURRENT_SCRIPT_INFORMATION_TEMPLATE = """
You are currently running the script with the following information:
- File Name containing services information: {{ file_name }}
- Maximum number of parallel checks:         {{ parallel_tasks }}
- Services Information:
      ------------------------------------
    {%- for service in services_information %}
      Address:  {{ service.address }}
      Port:     {{ service.port }}
      Protocol: {{ service.protocol }}
      ------------------------------------
    {%- endfor %}
"""
def print_summary_of_services_status(information : ScriptInformation, result : ResultInformation):
    print("Summary of Services Status")
    print("----------------------------")
    # In this case, we are not looping through the services_information list
    # But we are looping through indexes of that list.
    # We are using the indexes because we have to access the same index in
    ##both  the services_status list and the services_information list
    for i in range(len(information.services_information)):
        print(" Service at address ", information.services_information[i]['address'],
               " on port ", information.services_information[i]['port'] ,
               " is ", "UP" if result.services_status[i] else "DOWN",
               file=sys.stdout if result.services_status[i] else sys.stderr)

def store_the_results_in_a_file(information : ScriptInformation, result : ResultInformation):
    with open(information.file_name + ".json", "w") as file:
        json.dump(result.services_status, file, indent=4)

def prepare_the_output(information : ScriptInformation, result : ResultInformation):
    print_summary_of_services_status(information , result)
    store_the_results_in_a_file(information , result)

def inform_user_about_current_script_execution_information(information : ScriptInformation):
    template = jinja2.Template(CURRENT_SCRIPT_INFORMATION_TEMPLATE)
    print(template.render(information.__dict__))