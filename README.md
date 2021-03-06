# Lecture Notes & Work

+ 8/30 - Python fundamentals & work with git
  1. Make a new branch (git branch name, git checkout name)
  2. Write & commit (git add filename, git commit -m "message")
  3. Push to Github (git push)
  4. Merge to main on Github 
  5. Locally checkout to main (git checkout main)
  6. Pull from Github (git pull)

+ 9/1 - Modules
  + blood_calculator.py & database.py
  + Learned how to call functions from one into the other
  + Naming conventions of ^

+ 9/6 - Modular Code & Tags
  + Modular code is: Reusable, Testable, Readable
    + Don't want to have one function call another function call another function, it's less repeatable and harder to test/follow.
    + It's better to have return statements with inputs and outputs, with each function having inputs and outputs to ease testing (separate I/O from calculations, functions with defines arguments & returns)
  + Tags
    + git tag -a v1.0 -m "First release version with HDL/LDL/Total"
      + Tags WHOLE REPOSITORY with the tag, not specific file. 
      + When there is a particular commit to grade, tag it and push it up to Github.
  + GitHub Issues for Communication
    + Best way to communicate is to open a Github issue and tag the TAs/Dr. Ward. 
    + How to do it:
      + Click new issue in private repository
      + Title the issue & write explanation of issue
      + Go to code, click on the line, click on three dots, click on 'Copy Permalink'
        + Can use shift to select whole codeblocks
      + Paste permalink into the issue, which now includes line of code & link to the specific code
        + Points to exact problem on the exact branch
      + Click on assignees and choose the person you want a response from.  
+ 9/8 Lists, Mutable/Immutable
  + Lists
    + Can contain multiple datatypes
    + Use ```.append()``` command to add to the end of a list. 
      + Appends what is in the parentheses to the list that is dotted i.e. ```db.append(x)``` adds x to the end of the db list
    + To find last entry in a list, use ```list_name[-1]```. 
      + Can do -2 and get second to last in list, etc. 
      + Works with strings to get specific characters.
    + Can use indexing to go through indices of lists (and lists of lists) to get specific information
      + Use loops + if statements to pick out certain info
  + Immutable vs Mutable Objects
    + Integers are considered immutable. Can make variable a different number, but can't change value of number. 
    + Lists are mutable, they can be changed. 
      + b is pointing to the list
      + Put it into a and send to update()
      + Change value of list by adding 2
      + Now when printing b it is updated to now be original + 2
    + If a parameter is a string, integer, float, or boolean, it ***WON'T*** change in a function
    + If it's a list or a dictionary, it ***WILL*** change
  + BMI Calculator Homework Assignment
    + Python program that:
      + Received input from user from terminal window
        + Must take either kg/m or lb/in combination
      + Output to the terminal window the calculated BMI 
        + Go online to find the formula for BMI
      + Also output whether BMI is underweight, normal weight, overweight, obese
+ 9/13 Testing
  + Unit Testing 
    + To open: Make venv, install using requirements.txt
      + ```pytest```
      + ```pytest-pycodestyle```
    + To make a test function, make a genering python file with prefix *"test__"*
    + Make function called ```"test__function_name"``` (check out test_blood_calculator.py)
    + Better to make individual functions for each test rather than put multiple tests into the same function
    + Can use decorator (@), to run multiple test cases in the same test 
  + Style Guide
    + PEP-8 (https://www.python.org/dev/peps/pep-0008/)
      + Says how to indent code, how to comment, blank lines, etc.
      + To help code look neat and organized
      + After BMI, all code will need to meet PEP-8 standards
      + Can use pytest to catch PEP-8 errors and allow you to fix them
        + To run, in gitbash do ```pytest -v --pycodestyle```
  + Test Driven Development
    + Write unit tests ***BEFORE*** writing code bc you should know what code does/will do before writing it
    + Allows you to know what kind of input/outputs your function needs before writing it
+ 9/15 Robust Testing
  + Robust Testing
    + Need to capture different scenarios when creating tests.
    + Broad set of tests to test different possibilities of inputs. It's why parametrize is useful.
    + ```units = units.rstrip('s')``` changes "lbs" to "lb"
      + rstrip only strips it from the right, strip would do it wherever in the string
    + Can use pytest.approx(answer) to approximate the answer to what's expected. Useful for when using floats in test cases.
  + Continuous Integration Testing on Github
    + Can test locally, and locally in Github
    + In repository, make two directories. First mkdir .github. Next, enter that and mkdir workflows.
    + Enter that and create a new file by using touch filename.yml
    + Can make .github/workflow folder on main branch when creating a new repository. 
      + Along with README.md, requirements.txt, and .gitignore
  + Unit Testing & Continuous Integration Homework Assignment
    + Function called ```is_tachycardic``` in module ```tachycardia.py```
    + Function received a single parameter in a string, which will be a single word
      + Word may have random capitalization
    + If contains "tachycardic," it should return True
+ 9/20 - Dictionaries
  + Dictionaries
    + Use {} to access dictionaries, like this: oed = {"day": "when the sun is up", "night": "when the moon is out"}
    + What goes before the : is the '*key*' and what goes after is the '*value*'
    + To see what the keys are, call name.keys(). To see values, call name.values()
    + Easy to add to the dictionary, just type in a new key/value combo like this: oed["lunch"] = "what I will eat after class"
      + or like this: oed.get("lunch"); this prevents keyerrors for missing keys
    + Can store strings, ints, lists, etc. as a value in the dictionary
    + These values are MUTABLE
+ 9/22 - Exceptions and Logging
  + Exceptions
    + Two types of errors: syntax errors and exceptions
      + SyntaxError: interpreter doesn't even recognize what the module is trying to do
      + Exceptions: code runs, but it comes across an error in the code that will stop the program at that line
    + Types of exceptions:
      + IndexError (index didn't exist)
      + AttributesError (use a method on an object that doesn't have that attribute) ```hello.equals()```
      + ValueError (i.e. convert a string to an int, it's not a number)
      + TypeError (tried to add a string and a float)
      + AssertionError (```assert x == y```, if x != y then it's false, and an error)
      + NameError (wrong variable/function name)
      + KeyError (dictionary accessed with wrong key, or key doesn't exist)
      + ZeroDivisionError (can't divide by 0)
      + ModuleNotFoundError (try to import something that doesn't exist)
      + Can go to today's class notes on Exceptions and it will give some more examples of errors
  + Try Except Block (21 minute mark of Panopto lecture)
    + Tries to do something, looks to see if an error comes up, and executes a block of code in case
  + Can also load an error for the user when they do something incorrectly
    + Use an if statement and use ```raise``` with the error type
    + Can also add a message in the parentheses (```ValueError("message")```) to help the user
  + Next Homework Assignment: CPAP Analysis Program
    + Reads in CPAP data, analyzes the results, outputs results in separate output file for different patients
    + Read in data, must be flexible to handle any number of patients in the file with flexible lengths
    + Calculate average mask leakage
    + Calculate average events per hour
    + Based on the events avg at O2 data, decide 1/4 diagnoses.
    + Create an output json file 
      + Should include first name, last name, hours, seal, events, O2, seal average, diagnosis
      + Output ^ in a dictionary
+ 9/27 - Logging & Numpy/Matplotlib
  + Logging
    + Made fibonacci sequence, need to find a way to stop printing
    + Use python library called logging ```import logging```
    + Warning function: prints WARNING in front
    + Multiple levels: debug, info, warning, error, critical  
      + Default is to show warning and above. Can change by calling ```logging.basicConfig(level = logging.INFO)```
      + When setting level, use CAPS. When using function, use lower. 
    + Can save output to a .log file with ```logging.basicConfig(filename="example.log", filemode='w')``` to rewrite log file each time
+ 9/29 - ECG
  + ECG Assignment
    + PQRS signal
    + ![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/SinusRhythmLabels.svg/1200px-SinusRhythmLabels.svg.png "Logo Title Text 1")
    + Given data files that's a list of times and voltages (.csv comma separated text file)
      + First column is time in seconds, second column in voltage in mV.
    + Read in file
    + Perform calculations like: duration, find voltage max/min, number of heartbeats, average heart rate, list of times when beats occured
    + The above metrics should be stored as a dictionary and output as a .json file with the same name as the input file
    + There are directions for the README.md that are necessary for explaining how the code/algorithms work
+ 10/6 - Debugging & IDEs
  + Debugging
    + Code not behaving as expected, want to figure out why.
      + Print statements
      + Go through line-by-line
      + Can make logs
      + Make test cases
    + Make a new branch before debugging
    + Step over runs the function and continues through. Good to help with analysis to see which function creates the unexpected output.
    + Step into actually goes into that function and goes to the next line that will execute. 
    + Good flow is to step over, and then see if it created the bad results. 
      + If so, then redo and step into
      + If not, continue
    + Can keep track of variables on the side, check to make sure things are what they're expected to be
  + Debugging Approaches & Rules of Thumb
    + Understand the bug
    + Reproduce your bug
    + Examine your assumptions
    + Determine the location of the error/fault
+ 10/11 - APIs, Intro to Web Services, Requests
  + APIs (Applicable Programming Interface)
    + Physical example: microwave
      + Interact with it by pressing buttons on the control panel (input)
      + Receive some result on the digital display (output)
      + When start is pressed, microwave does a ton of functions:
        + Is door closed? Turn on light. Turn on microwave generator. Start timer. Rotate platform. Turn off microwave generator. Beep.
    + Software example: SciPy
      + Call an "exposed" function that then calls hidden underlying functions that access the functionality of the package.
    + Designing an API
      + Keystones of APIs are functions.
      + As an API designer, need to consider:
        + Which functions are exposed to the user
        + How to ensure API functions are flexible enough to be "stable" for some amount of time 
        + Platform independence 
  + Web Services
    + Modern software design uses cloud computing
    + RESTful APIs: **RE**presentational **S**tate **T**ransfer
      + Instead of installing packages onto our local computers, we call RESTful APIs to call functionality in the cloud
    + **URL**: Uniform resource locator. URLs can be thought of as function names to access functionality on a server.
      + http://vcm-7631-vm.duke.edu:5000/sum
      + Protocol for transfer (http)
      + Domain name (duke.edu)
      + Sub-domain name (vcm-7631-vm)
      + Port (5000)
      + Path/Route (sum)
    + **Client**: Computer or local software that wants to share information with web server or service
    + **Web server or service**: program running on separate machine
    + **Reqest**: sent from client to server to access
    + **Response**: sent from server to client
  + Requests
    + ***GET***: generally used to get information from a server
    + ***POST***: Generally used to send info to server and perhaps receive something, used for data storage
  + Actual work for today:
    + Add ```requests``` to requirements.txt 
    + Work done in ```github_access.py```
+ 10/13 - Web Servers
  + Flask - a Python package that allows us to create a web service/server that can expose a RESTful API
    + First need to install ```flask``` into virtual environment
    + ```Flask, request``` is different from ```requests```
+ 10/18 - Server Design
  + Need to write code that returns errors to client so they know what to fix
+ 10/20 - Virtual Machines
  + Allows other people to access server on your laptop by moving it to a virtual machine instead of your computer.
+ 10/25 - Databases
  + Relational and non-relational
    + Relational (SQL) - have a pre-defined structure (schema)
      + i.e. comes with predefined categories like "Name", "Age", "SSN", etc.
    + Non-relational (NoSQL) - no pre-defined structure
      + each entry is an "object"
      + data is often stored in key-value pairs
      + Advantages: different objects can have different information, easy to change
    + We'll use non-relational DB called MongoDB