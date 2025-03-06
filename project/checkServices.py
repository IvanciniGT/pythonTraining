from models.script_information import ScriptInformation
from models.result_information import ResultInformation
from tasks.check_tasks import check_all_services
from tasks.validation_tasks import validate_my_script_information
from tasks.output_tasks import prepare_the_output, inform_user_about_current_script_execution_information
from tasks.read_tasks import read_all_the_script_information

# This right here is like the INDEX of a BOOK
# It allows you to have a quick overview of the script
def my_script():
    information : ScriptInformation = read_all_the_script_information()
    validate_my_script_information(information)
    inform_user_about_current_script_execution_information(information)
    result : ResultInformation = check_all_services(information)
    prepare_the_output(information, result)

my_script()

