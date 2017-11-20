======
Weaver
======

Weaver has two main goals

Bootstrapping my Development Environment
  To enable ansible / salt like bootstrapping of my local workstation, and by
  extension my target servers

Maintaining my Development Environment
  To enable a consistent pre- and post- commit process, ensuring linting etc
  are done correctly, commit messages are properly formatted etc.

Migrating to Fedora
-------------------
For various boring reasons I am migrating to use a Fedora workstation.
This means I need to adjust apt-get to yum (I want weaver to remain simple so I am reluctant to jumpt tosome kind of "detect OS and do different things" approach)


initial start up
This is asuming a clean machine.

* from my personal USB stick, install my own .ssh folder.
* I might also install a start up script ?


start up script

* can I see "the internet"?
ping 8.8.8.8

* can I see github
ssh -T git@github.com
-> this shows I have both a internet connection and a ssh private key (id_rsa?) that has a finger print registered with github


Python install
--------------

We have python (2.6.1) and python3 (3.6.1)


 am aiming for python3 as base standard
So that means my develop,emtn work will be in pyhton3, and I need venvs in p3

* SO we need to install pip3 from the package manager
* then from pip3 install virtualenvrapper (/usr/bin/virtualenvwrapper)


-------------------
Bootstrap to weaver
-------------------

Obviously we do not start with `weaver` installed, so we need to lay out the
(manual / to be automated) steps first.  In past incarnations I have used
kickstart and PXEBoot to install OSes etc.  This will have to be re-remembered.


* python setup.py develop
This (in a venv) will install weaver so that the realtive imports work ok
See https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install on fixing realtive imports

* I need to convert to python 3 - all my pront stmts are wrong


0. Validate Hardware, safeboot etc
   There is a very valid concern that any modern mainboard has a proprietary
   and un-verifiable (and probalby insecure) OS - usually the Intel ME engine
   or similar.  Additionally UEFI like secure boot services need to be verified.
   I am not dealing with this here, but is covered in "The Software Mind".

1. Install OS
   For now we use a simplistic Ubunutu on USB stick

1.a. Update OS
   TBD

1.b. Harden OS
   TBD

2. Install weaver

3. Install further local environments

Keeping secure stuff secure
---------------------------

This is purely for local laptop issues.
But I want to have some level of secure stuff, that can be on disk but not kept in git(hub)
These will be

* passwords to web services
* ssh keys and similar

I *think* I want an encrypted file(system?)
I *think* I need to store them on USB key
And then open up on disk after I install?
Look into this further
   


A discussion on local environments
==================================

We no longer want to install stuff onto a OS's local system.  We want to
partition / seperate from the local system, often not using /etc and so on
but keeping everything in "our" tree.

There are two main local environemnts I am discussing here - a `python virtual
environment` and a container such as FreeBSD jail or linux Docker (lxc)

I expect to develop local services, mostly weaver, as python venvs, and everything
else as python venvs deployed into docker for ease of futrure deployment.

I expcet to use pyHolodeck to bundle up venvs as .debs




* install OS
  DOne thru manual install (ubuntu)
  TODO:

* base install framework
  I intend to use python's `fabric` for the day to day installation and update.
  It is roughly analogius to ansible without the hype and I see no major reason to
  jump bandwagons.

  Before we get there we need a decent python set up

  The file ``early_install_pyvenvs.sh`` should be run first
  Then we have a pip / venv environment
  Then we can pip install weaver.  For now I am running it locally

  pip install fabric3 sphinx

  We are following the python3 fork of fabric, and hope for a nice merge in the future.

  weaver
  ------
  this is installed using pip install -e /path/to/pkgdir
  this gives me a development environment to work on
  I do not have to reinstall to see changes take effect
  I have added a "entry point" in the setup.py file such that (in the right venv) I can call
  weaver and installs will occur

  All the rest of the installs and configs should be conducted with weaver from now on
  and the python apt library


* SSH and identities

* git, source code etc

* atom / emacs

* pyholodeck and docker
