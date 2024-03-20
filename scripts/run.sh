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


# run the application
/usr/bin/python3 /Users/USER/Desktop/dev/ele-525-project/main.py