#: Install pip and virtualenvs

sudo yum check-update
sudo yum install python3-pip python3-devel python3-tools git-core -y
sudo yum install gcc gmp redhat-rpm-config -y #needed for building pycrypto on fedora
sudo yum install -y isomd5sum
sudo pip3 install virtualenv
sudo pip3 install virtualenvwrapper

VENV=~/venvs
mkdir -p $VENV

echo "export VIRTUALENV_PYTHON=/usr/bin/python3.6" >> ~/.bashrc
echo "export WORKON_HOME=$VENV" >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_VIRTUALENV=/usr/bin/virtualenv" >> ~/.bashrc

echo "source /usr/bin/virtualenvwrapper.sh" >> ~/.bashrc
echo "export PIP_VIRTUALENV_BASE=$VENV" >> ~/.bashrc



# set fabric settings


source ~/.bashrc

chown pbrian:pbrian -R $VENV

#: openssh-server
sudo yum install openssh-server -y
#: configure sshd (its usually pretty good so nothing needed right now)
# now we can use fabric form the python install above to connect to the
# sshd on localhost - all further work can be done via fabric to localhost
