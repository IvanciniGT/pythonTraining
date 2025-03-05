# Imperative programming


service_name = "oracle"
service_domain = "localhost"
service_port = 1521
service_protocol = "tcp"

service_status = True

if( service_status ):
    print("The service "+service_name+" is running")
else:
    print("The service "+service_name+" is not running")

service_name_2 = "mysql"
service_domain_2 = "localhost"
service_port_2 = 3306
service_protocol_2 = "tcp"

service_status_2 = False

if( service_status_2 ):
    print("The service "+service_name_2+" is running")
else:
    print("The service "+service_name_2+" is not running")

# Procedural programming
# I need to deal with a service information
# I need to store the name of the service
# I need to store the domain(IP) of the service
# I need to store the port of the service
# I need to store the protocol of the service

def is_service_running( service_name, service_domain, service_port, service_protocol ):
    # Somehow... from python I have to connect to the service and check if it is running or not
    # At least to check whether that port is open or not
    # We are not going to do that right now (we will.. on Thursday)
    return True


# I want to print whether each service is running or not
# In order to do that... I could create a second function that receives the service status and prints a message
def print_service_status( service_name, service_status ):
    if service_status:
        print("The service "+service_name+" is running")
    else:
        print("The service "+service_name+" is not running")


service_name = "oracle"
service_domain = "localhost"
service_port = 1521
service_protocol = "tcp"

# I have a second service that I want to check if it is running or not
service_name_2 = "mysql"
service_domain_2 = "localhost"
service_port_2 = 3306
service_protocol_2 = "tcp"

# now... I want to know if that service is running or not
# In order to do that we could create a function that checks if the service is running or not
# Now I can make use of that function to check if the service is running or not
service_status = is_service_running( service_name, service_domain, service_port, service_protocol )
service_status_2 = is_service_running( service_name_2, service_domain_2, service_port_2, service_protocol_2 )
print_service_status( service_name, service_status )
print_service_status( service_name_2, service_status_2 )

### But... there is something in that code... that smells... really bad
### Another bad practice:
### We should never have to supply more that 2/3 arguments to a function

# To solve this situation... a better approach would have been to pack all the information of the service together

# We already know how to pack a bunch of information together... using a dictionary
oracle_service = {
    "name":     "oracle",
    "domain":   "localhost",
    "port":     1521,
    "protocol": "tcp"
}

mysql_service = {
    "name":     "mysql",
    "domain":   "localhost",
    "port":     3306,
    "protocol": "tcp"
}

print(oracle_service["name"])
print(mysql_service["port"])

def is_service_running( service_information ):
    service_information["status"] = True

def print_service_status( service_information ):
    if service_information["status"]:
        print("The service "+service_information["name"]+" is running")
    else:
        print("The service "+service_information["name"]+" is not running")

is_service_running( oracle_service )
is_service_running( mysql_service )

print_service_status( oracle_service )
print_service_status( mysql_service )

# This is nice!!!!
# But... there is a problem with that... And a big one.
# We have no control at all of the keys of the dictionary

# Let's try another approach... let's go for Object Oriented Programming
# Let's create a Class that represents a service
# When creating a class, we always start the same way.
# We will define a function to instruct python how a new instance (object) of that class should be created
# That function is called a CONSTRUCTOR. In python the constructor is a function called __init__
class Service:
                # self is a special keyword... It points to the object itself
                                             # It's better if you think at first in that "self" 
                                             # keyword as a dictionary associated to each object of that class
    def __init__(self, name, domain, port, protocol):
        
        self.name       = name              # We are just storing the values in the object dictionary
        self.domain     = domain            # By the way, we are storing also the "status"
        self.port       = port
        self.protocol   = protocol
        self.status     = None

    def is_running( self ):
        self.status = True

    def print_status( self ):
        if self.status:
            print("The service "+self.name+" is running")
        else:
            print("The service "+self.name+" is not running")

# At this moment we have defined a class... 
# And right now we can start creating objects of that class (instances of that class)... actual data.
oracle_service = Service("oracle", "localhost", 1521, "tcp") # Internally, python is going to call the __init__ function
                                                             # with the values we are providing as arguments
mysql_service  = Service("mysql", "localhost", 3306, "tcp")
# ^^^ This points to that recently created `dictionary` associated to the object

# Actually in python in order to create a string... we could write
my_string      = str("Hello World")
my_number      = int(1)

oracle_service.is_running()
mysql_service.is_running()

oracle_service.print_status()
mysql_service.print_status()

############ Final code

class Service:

    def __init__(self, name, domain, port, protocol):
        self.name       = name
        self.domain     = domain
        self.port       = port
        self.protocol   = protocol
        self.status     = None

    def is_running( self ):
        self.status = True

    def print_status( self ):
        if self.status:
            print("The service "+self.name+" is running")
        else:
            print("The service "+self.name+" is not running")


oracle_service   = Service("oracle", "localhost", 1521, "tcp") # Internally, python is going to call the __init__ function
mysql_service    = Service("mysql", "localhost", 3306, "tcp")
nginx_service    = Service("nginx", "localhost", 80, "tcp")
apache_service   = Service("apache", "localhost", 8080, "tcp")
postgres_service = Service("postgres", "localhost", 5432, "tcp")
redis_service    = Service("redis", "localhost", 6379, "tcp")
#
# ping 
# telnet
# curl

oracle_service.is_running()
mysql_service.is_running()
nginx_service.is_running()

oracle_service.print_status()
mysql_service.print_status()
redis_service.print_status()
