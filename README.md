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