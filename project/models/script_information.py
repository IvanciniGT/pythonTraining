# Information???
# - FileName
# - ServicesInformation
# - How many tasks do we want to run in parallel?

class ScriptInformation:
    
    def __init__(self, file_name, environment_variables, services_information ):
        self.file_name = file_name
        self.services_information = services_information
        self.parallel_tasks = environment_variables["parallel_tasks"]
