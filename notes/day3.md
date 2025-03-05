- We need to work more on OOP
- We have to learn how to invoke different processes (from python) and how to communicate with them
- Working with threads!
- Working with FILES (TEXT, JSON, YAML)


---

# THREADs

Each Operating system allows us to manage processes.

A process is a running program.

Each time we ask the OS to run a program, the OS creates a process.

Each process always has at least one thread.

A thread is what the OS uses to run the code.

Our code is getting run by a thread.

A thread is kind a little person inside the computer that is running our code.

The program does not execute itself. 
The program is just a DOCUMENT... same as a cooking recipe.
We need someone to read the recipe and execute the steps. That's the thread.

Threads live inside processes.
The OS, when creating a process, creates a main thread associated with that process.
That main thread is the one that starts running the code (the program).

But, under certain circumstances, we can create more threads.
It's the same as having more people cooking in the kitchen... the same recipe.

For sure we could also have different recipes running at the same time. And different people cooking each recipe.

One thread can only perform one task at a time.
If we to execute several tasks at the same time, we need to create more threads.

There's a problem with this.
To open new threads is easy.
The problem is that we will need to synchronize the threads.

Imagine again, our recipe example.
We have 2 people cooking the same recipe.
Imagine we are cooking some kind of pasta.

- On guy is boiling the water, and taking care of the pasta.
- The other guy is preparing the sauce.

Once both have finished their tasks, I can continue with the recipe.


---

Python Built-in functions...
As you can imagine, Python has a lot of built-in functions.
To make it easy to work with them, they are organized in "modules".

---

The good practice in Python es to name:
- variables with snake_case: All characters are lowercase, and words are separated by underscores.
- functions with snake_case
- Classes with CamelCase: The first letter of each word is capitalized, al words are together.

Those rules change from language to language.

| LANGUAGE      | VARIABLE                            | 
|---------------|-------------------------------------|
| Python        | we_name_a_variable_like_this        |
| C             | we_name_a_variable_like_this        |
| C++           | we_name_a_variable_like_this        |
| Java          | weNameAVariableLikeThis             |
| Visual Basic  | WeNameAVariableLikeThis             |

We need to respect those conventions to make our code more readable.
In python they are called "PEP8" rules.

---

# Let's work with processes

As we said before... an OS starts a process when we ask it to run a program.
We usually ask the OS to run a program by using the command line....
also by clicking on an icon, or by double-clicking on a file.
But we can also ask the OS to run a program from another program.
An that's what we are going to do now.

          OS
          -------------------------------------------

                    +---------------------+
                    |                     |
    Standard Input   >     PROCESS         >   Standard Output
       Channel      |                     |    Channel   (1)
         (0)        +----------V----------+
                        Error Channel  (2)


That thing (about communication channels) is valid for all OSs (windows included).
In addition, once a process ends it returns a number.
That number is called "exit code" or "return code".

If that number is 0, it means that the process ended successfully.
If that number is different from 0, it means that the process ended with an error.
Depending on the error... each process will return a different number.
Each program has its own error codes.
But for all of them, in every single OS, 0 means success.


In linux we can get that number by using the command "echo $?".
In windows we can get that number by using the command "echo %ERRORLEVEL%" (command prompt) or "echo $LASTEXITCODE" (powershell).


> bash
>
> my_command 1> output.txt 2>&1
> # When we use pipes
> my_command | grep "something"
>
> .bat
> .sh       SCRIPT



One thing about python script is that they work in every OS.
I just need to have python (a python interpreter: cython) installed in the OS.

Once said that... we should try to avoid calling external programs from python 
CASE WE ARE CREATING ANS SCRIPT THAT SHOULD RUN ON EVERY OS.

Because it's hard to make sure that the program we are calling is installed in every OS.

Instead of doing that... we should try to find a python module that does the same thing that the external program does.

As I told you... we have thousands of modules in python.
Python ships with a lot of modules.

We usually install third-party modules by using the command "python -m pip install MODULE".

Where those modules are located? in the "Python Package Index" (PyPI).



----

On day 1, you all said to me that you were here because you want to use python for Automation.
That's great.

# What's is DEV-->OPS?

Devops is a culture... it is a philosophy.... it's a way of working... it's a movement....
defending WHAT??? AUTOMATION

Ey guys! Let's automate everything... from DEV to OPS.

Time AGO, when developers where thinking about a software LIFE CYCLE, they were thinking about:
- A SEQUENCE OF PROJECTS (ruled by a Waterfall methodology)


AUTOMATION is just a process that implies:
THE CREATION OF A MACHINE (or a program that can change the behavior of a machine) that can do a task that time ago was done by a human.

In our case, to automate a task means: TO CREATE A PROGRAM THAT CAN DO A TASK THAT TIME AGO WAS DONE BY A HUMAN.

I can do that with :
- Ansible
- Puppet
- Terraform
- Chef
- BASH scripts
- Powershell scripts
- command line scripts
- Python scripts <<<<<<<< THIS IS A GENERAL PURPOSE LANGUAGE
                          I can do whatever I want with python.
                          For sure... I have other tools right there that speak a higher level language than python.
                           