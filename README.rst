======
Weaver
======

Its for managing (at the moment) my local laptop, and acting as a kind
of `phab` tool - running unit tests etc for me.

At the moment my goal is to allow myself time to build things
correctly, so I want to be able to *re*build things easily.

Weaver uses Fabric3 not the official fabric 1.x (using python 2) I am
not clear on why official fabric is still on 2.x but there we are.


The start from Scratch guide to Weaver
--------------------------------------

So, I am going to re-build my tools.  Initially this is rebuilding
laptop, but it will move to re-building iPhone etc.  THe goal is to be
N+1 reliable.

1. Installing Fedora So I have not built a kickstarter script (at
least not for a decade) but we shall just do a manual install for now.
Having done a manual install (settings were ??) I then use my backup
USB stick, formatted as DOS, and load up my .ssh, and projects file.

(I guess I dont need the projects file as they are on github)

Starting with Weaver
--------------------



examples::

    weaver todo .
    #will parse all todo information in source trees under .
    and return a sensible todo list


    weaver clean --dev .
    # will walk below tree . and remove all files meeting either .gitignore
    or .weaver.clean globs

    
