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
