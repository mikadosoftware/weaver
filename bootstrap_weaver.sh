#: Install pip and virtualenvs
sudo apt-get update
sudo apt-get install python-setuptools python-dev build-essential git-core python-apt -y
sudo easy_install pip
sudo pip install virtualenv
sudo pip install virtualenvwrapper
VENV=~/venvs
mkdir $VENV
echo "export WORKON_HOME=$VENV" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
echo "export PIP_VIRTUALENV_BASE=$VENV" >> ~/.bashrc
source ~/.bashrc
chown pbrian:pbrian -R $VENV

#: openssh-server
sudo apt-get install openssh-server
#: configure sshd (its usually pretty good so nothing needed right now)
# now we can use fabric form the python install above to connect to the
# sshd on localhost - all further work can be done via fabric to localhost
