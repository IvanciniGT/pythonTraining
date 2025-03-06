from models.script_information import ScriptInformation
import socket 
from threading import Thread

from models.result_information import ResultInformation

CONNECTION_TIMEOUT_IN_SECONDS = 5


class ServiceChecker(Thread):
    def __init__(self, services, results):
        super().__init__()
        self.services = services
        self.results = results
    
    def run(self):
        # Here's where this checker will check the services... 1 by 1... while there are services to check
        while (self.results.last_service_checked < len(self.services)):                  # While there are services to check
            self.results.last_service_checked += 1                                       # Get the next service to check
            current_index = self.results.last_service_checked
            if(current_index >= len(self.services)):                                      # If there are no more services to check
                return # To solver what we called a running condition. 
                       # When 2 threads come to this point, at the same time, one of them needs to return... 
                       # because the other one will take care of the last service
            next_service_to_check = self.services[current_index]
            result=check_service(next_service_to_check)                                  # Check the service
            self.results.services_status[current_index] = result             # Store the result in the results list

def check_service(service):
    # Here is where we are going to open a connection to the service (Socket), to check whether it is open or not

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:    # We open a socket ... It will be closed automatically
        my_socket.settimeout(CONNECTION_TIMEOUT_IN_SECONDS)                 # We set a timeout for the connection
        try:
            my_socket.connect((service['address'], service['port']))        # We try to connect to the service
            return True                                                     # If we can connect, the service is running
        except:
            return False                                                    # If we can't connect, the service is not running           

def check_all_services(information : ScriptInformation):
    results = ResultInformation(len(information.services_information))
    
    # I create all the checkers (threads) that will check the services
    checkers = []
    for checker_number in range(0,information.parallel_tasks):
        checker = ServiceChecker(information.services_information, results) # Here's where we create a checker
        checker.start()                                                    # Here's where we start the checker (thread).. this executes the run method
        checkers.append(checker)                                           # I store a reference to the checker (thread)

    # I will wait for them all to finish
    for checker in checkers:
        checker.join()
    
    return results

