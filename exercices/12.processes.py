import subprocess

# curl https://google.es to check whether our server has internet connection or not

command = ["echo","Welcome to the jungle"]

# The subprocess module allows us to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

try: 
    result = subprocess.run(
                                command,                # The command to run
                                capture_output=True,    # Capture the output of the command
                                text=True,              # The output will be text
                                timeout=10              # Case the command takes more than 10 seconds to run
                        )                            # The run function will raise a TimeoutExpired exception

    # The `result` variable allows me to :
    # - Know the return code of the command
    print("The return code of the command was: ", result.returncode)
    # - Know the output of the command
    print("The output of the command was:      ", result.stdout)
    # - Know the error of the command
    print("The error of the command was:       ", result.stderr)
except subprocess.TimeoutExpired as e:
    print("The command took too long to run")
except Exception as e:
    print("Generic exception: ", e)
