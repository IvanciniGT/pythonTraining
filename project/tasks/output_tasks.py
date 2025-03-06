import jinja2
from models.result_information import ResultInformation
from models.script_information import ScriptInformation

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


def prepare_the_output(information : ScriptInformation, result : ResultInformation):
    print("Preparing the output")
    #print_summary_of_services_status
    #store_the_results_in_a_file

def inform_user_about_current_script_execution_information(information : ScriptInformation):
    template = jinja2.Template(CURRENT_SCRIPT_INFORMATION_TEMPLATE)
    print(template.render(information.__dict__))