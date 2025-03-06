

class ResultInformation:
    
    def __init__(self, number_of_services):
        self.last_service_checked = -1
        self.services_status = [False] * number_of_services
                       # This creates a list containing `number_of_services` False values
                       # [ False, False, False....] 
