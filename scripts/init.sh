#!bin/bash

# Set the default shell to zsh

# see if python and pip are installed, else thro error 
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed"
    exit
fi

if ! command -v pip3 &> /dev/null
then
    echo "Pip is not installed"
    exit
fi

# Install the required packages
pip3 install -r requirements.txt
