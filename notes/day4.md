We have been learning about:
- Data and Data Types: strings, integers, floats, booleans, lists, dictionaries, tuples...
- Variables: how to name them, how to assign values to them, how to use them...
- Operators: arithmetic, comparison, logical, assignment, 
- Control Structures: if, else, elif, while, for
- Functions: how to define them, how to call them, how to pass arguments to them, how to return values from them...
- Functional programming: map, filter, supplying functions as arguments to other functions...
- Modules: how to import them, how to install them, how to use them... (import MODULE     from MODULE import FUNCTION, CLASS)
- OOP: how to define classes, how to create objects, how to use objects, how to define methods, how to use methods...
       how to extend classes, how to override methods, how to use inheritance, how to use super()...
- Files: how to open them, how to read them, how to write to them, how to close them...
         Create directories, remove directories, list directories, change directories...
         Move files
- Deal with environment variables
- Formats: JSON and YAML
- Templates: Jinja2
- Threads: how to create them, how to synchronize them...
- Processes: how to create new ones, how to interact with them...

# Our project:

Let's create an script.
We want to monitor some services... whether they are running or not.
The point here is that those services will be defined in a file (YAML).
We will need to read that file, and based on the information there, we will need monitor those services.
But... we will do that not 1 by 1... we will do that in parallel... we could process them 5 by 5... or 10 by 10....
Actually, we will read that information (that number) from an environment variable.
The file is gonna be called as the user wants... the user just need to provide the name of the file when running the script:
 $ check services.yaml
 $ check databases.yaml

We will need to TRY to open a socket! to the IP/PORT of the service (as declared in the file).
If we can open the socket, we will mark the service as "up".
If we can't open the socket, we will mark the service as "down".

Right after that we will create a report... a file with the status of the services.
Actually... we can create a JSON FILE With that information.
In addition, we will display through the standard out of the console the status of the services that are running.
And, we will display through the standard error of the console the status of the services that are not running.

Case all services are running, our script will finish with a 0 exit code.
Case the file provided by the user when calling the script (services.yaml) does not exist, our script will finish with a 1 exit code.
Case any of them is not running, our script will finish with a different exit code: 2

THAT's IT !

 $ monitor services.yaml 5

This one right here is almost the same as the previous one...
The difference is that we will monitor the services in a loop.
We will monitor the services every 5 seconds (An additional argument will be provided by the user).


# Custom modules

We usually create custom modules to keep our code organized.
We can create a folder... ith whichever name we want.
Inside that folder we can play a bunch of python files.
There is one important file that needs to be there... even if it is empty: __init__.py