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