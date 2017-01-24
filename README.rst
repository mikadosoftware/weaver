======
Weaver
======

An extensible developer helper command line tool

examples::

    weaver todo .
    #will parse all todo information in source trees under .
    and return a sensible todo list


    weaver clean --dev .
    # will walk below tree . and remove all files meeting either .gitignore
    or .weaver.clean globs

    
