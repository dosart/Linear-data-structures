 #!/usr/bin/env bash

checkStringAndWrite() {
if grep -Fxq "$1" ~/.bashrc
then
    echo "Exist: " $1
else
    echo >> ~/.bashrc
    echo $1 >> ~/.bashrc
fi
}

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

echo "Installing curl."
sudo apt install -y curl

echo "Installing poetry."
curl -sSL https://install.python-poetry.org | python3 -

echo "Adding poetry to PATH."
export PATH="/home/vagrant/.local/bin:$PATH"
checkStringAndWrite 'export PATH="/home/vagrant/.local/bin:$PATH"'

echo "Loading terminal prompt formatting from .bash_prompt."
checkStringAndWrite "# load terminal prompt formatting from"
checkStringAndWrite "source ~/.bash_prompt"
sudo ln -s /vagrant/.bash_prompt ~/.bash_prompt
source ~/.bashrc

echo "Installing pip."
sudo apt-get -y install python3-pip

echo "Installing pre-commit."
pip install --user pre-commit
cd /vagrant
pre-commit install

echo "Installing project dependencies and activating the virtual environment."
poetry config virtualenvs.in-project true
poetry env use python3.8
poetry install
poetry shell

