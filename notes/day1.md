
# Python

Python is programming language...
A language has a GRAMMAR:
- TOKENS: words, numbers, symbols
- SYNTAX: rules for writing messages
- SEMANTICS: meaning of each token... 

In programming languages we use different taxonomies:

## Interpreted vs Compiled

Computers, they don't understand Python, nor Java, C... 
Each computer speaks in its own language, that language dependes on the architecture of the computer and the Operating System.

So... We want to create programs that will be handle by the computer... but the computer is not able to understand our language... (PYTHON, JAVA, C, etc.)

So... we have to TRANSLATE from our language to the computer language...
We could do that in 2 completely different ways:
- Compilation. Translate our code (from python) to the computer language (binary code) before delivering it to the computer.
  EXAMPLES: C, C++, Fortran
- Interpretation. Translate our code (from python) to the computer language (binary code) while the computer is running the program. In order to do interpretation, we need an interpreter.
  EXAMPLES: Python, JavaScript 

    In python we have a bunch of interpreters that we can install (cython, jython, pypy, etc.)
    The most used is Cython, which is the official interpreter of Python.

  Compiled + Interpreted = JAVA

## High-level vs Low-level

- Low-level languages are closer to the computer language, they are more difficult to understand and to write, but they are more efficient.

- High-level languages are closer to human language, they are easier to understand and to write, but they are less efficient.

Automation script... 
    In C... maybe that program could take less than 20 seconds to run.     
            maybe we will need 30 hours to write it.
    In Python... maybe that program could take more than 25 seconds to run.
            maybe we will need 2 hours to write it.

## General-purpose vs Domain-specific

- Domain-specific languages are designed to solve a specific problem.
- General-purpose languages are designed to solve a wide range of problems: PYTHON

## Typed vs Untyped (static vs dynamic)

When we create software we deal wth DATA.
That DATA will have a nature, a type:
- TEXT
- NUMBER (integer, decimal)
- LOGICAL VALUES (BOOLEAN): true/false
- DATE

That true for every single programming language.

But... in order to refer to that data, we need to give it a name, a label, a variable.

```java
    String name = "John"; // Statement (Sentence in Python)
    name = 4; // WE HAVE A PROBLEM HERE! THIS IS NOT ALLOWED BY THE SYNTAX OF JAVA
```
1º "John"            This creates a new DATA in memory (RAM)... a TEXT data, with value: "John"
                        RAM memory is like a notebook, where we can write and read data.
                        The computer (OS) opens that notebook (I don't really know where it is) and writes "John" in it.
2º String name       This creates a new VARIABLE with name "name".
                        A variable (IN JAVA, PYTHON, JS) is like a postit.
                        What we are doing here is to take one of those postits and write "name" in it.
                        In our case (the upper one) We are writing JAVA code... and we are telling the computer to get a Postit from the green block and write "name" in it.
                        Green postit may point to String (TEXTS)... actually thet can only point to texts.
                        If we want to point to numbers, we may need to get a postit from the yellow block.
                        If we want to point to logical values, we may need to get a postit from the blue block.
3º =                 This is the ASSIGNMENT operator. We are assigning the variable "name" to the data "John".
                        We paste the postit "name" in the page "John" in the notebook.

So next time I need to refer to "John", I will tell the computer, ey! just go to that notebook (RAM) and get whatever information beside a postit with the name "name".


The concept of variable changes from one language to another.
- A variable is like a "box", where we can store data, to be used later. Thant's true... IN C. Not in python
- In python (JS, JAVA) a variable is a pointer to a data. 

    Assigning "John" to the variable name.  This is what happens in C
    Assigning the variable name to "John".  This is what happens in Python, JS, Java



In typed languages, variables have a type, and that type is defined when we create the variable.

In contrast, in untyped languages, variables don't have a type.


```python
    name = "John" # Statement (Sentence in Python)
    name = 4; # THIS IS OK!
```

```python
    name = "John"
    name = "Brenda"
```

First line:
1. "John" is created in memory
2. name variable is created 
3. name is assigned to "John"

Second line:
1. "Brenda" is created in memory.. RELEVANT QUESTION HERE IS: Where is "Brenda" stored in RAM?
                                   Does it overwrite "John"?
                                   Or is written in a different page? CORRECT
2. name is assigned to "Brenda"    We just move the posit... We reassign the variable

At this point! in memory we have 2 TEXTS: "John" and "Brenda"
But... there is no postit (variable) pointing to "John" anymore.
In Java, JS, PYTHON, there is no way to access "John" anymore.
 (BTW: In C we can access "John" by using the memory address)
That value is considered garbage.
Any value (DATA) that is not accessible by the program is considered garbage.
And PYTHON, JAVA, JS they do have a garbage collector that eventually will clean that garbage (or not).

Untyped languages have a huge problem ... I cannot use them when working on a big project... or in a project that will be maintained by different people.

    function generateReport(title, data):             <--- in python
        Title could be the actual title of the report.
        But it may be whether we want a title or not.
        This function creates a report in PDF... It returns that report? Or maybe it is stored in a file somewhere?

    boolean generateReport(String title, int[] data){}             <--- in java

### Paradigms: Procedural, Object-oriented, Functional, Logical, etc.

`Paradigm` is just another fancy word that people use in this software development world to refer to a way of communicating an idea.

We do have that same concept in human languages: English, Spanish, French, etc.

Imagine this sentence... in English: "Peter, place a chair under the table"        Imperative: Order
                                     "Peter, you are responsible for placing a chair under the table. And I want a char under the table, right now!"        Declarative: Statement

In programming languages:
- Imperative:               We tell the computer what to do, step by step (statement by statement)
                            Sometimes we need(want) to break the sequence of statements... and we use of special word that we have in almost every single programming language: 
                                - CONDITIONALS: if, else, switch    \
                                - LOOPS: for, while                 /  Control flow statements
- Procedural:               We may want to pack a bunch of statements ... 
                            So we can refer to them by using a single word: PROCEDURE/FUNCTION/RUTINE/METHOD.
                            We may want to do this :
                                - To be able to reuse that code
                                - To make the code more readable and maintainable
                                - When a language allows us to define functions... and to execute them afterwords... we say that that language is procedural.
- Functional:               Functional programming is not PROCEDURAL PROGRAMMING.
                            The ability to define and execute functions is called PROCEDURAL PROGRAMMING.
                            Functional programming is a different thing... It is an evolution of procedural programming.
                            We cannot have functional programming without procedural programming.
                            The concept is extremely simple...
                            When a programming language allows us to point a variable to a function, and to execute that function by using that variable, we say that that language supports functional programming.
                            The point with functional programming is not what it is...
                            The point is what we can achieve with it.
                            And here is when our brains explode!!! Get ready!!!

                            Once a programming language allows us to do that... then:
                            - We can start creating functions... allowing other functions as arguments
                            - We can start creating functions... returning other functions

                            WHAT!!!???? 

                            In functional programming functions are first-class citizens.

- Object-oriented:          Every single programming language allows us to deal with data.
                            And every single programming language ships with a bunch of data types.
                            Some programming languages allow us to create our own data types, 
                            with its own characteristics and behaviors.
                            When a programming language allows us to create our own data types, we say that that language is object-oriented. Custom data types are called CLASSES.

                                Datatype    Characterized:              Operations:
                                String      a sequence of characters        Concatenation, toUpperCase
                                    "Brenda"
                                    "John"
                                    "hi"
                                Numbers     a numeric                       sum, multiply
                                    3
                                    -18.8
                                Dates       a day, a month, a year          difference, addDays
                                -----------------------------------------------------------------------
                                Machine     IPs, fqdn, admin-user           connect, disconnect, ping
                                 (server)
                                    mySMTPServer is an instance of a Machine
                                     ^^^^^^^^^^                      ^^^^^^^
                                     OBJECT                          CLASS
---

Software types:
- Operating Systems
- Drivers
- Applications
- Libraries
- Scripts **** 20Kbs - 100Kbs
- Commands
