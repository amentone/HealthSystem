#!/bin/bash
#
# Be sure if you are in HealthSystem dir before starting this script!
#
VENV="virtualenv -p python3 venv"
#
# Check for dependecies:
command -v python3 > /dev/null 2>&1 || { echo >&2 "Python 3 needed: check your distro for installation guide."; exit 1; }
command -v pip3 > /dev/null 2>&1 || { echo >&2 "Python 3-pip needed: check your distro for installation guide."; exit 1; }
command -v virtualenv > /dev/null 2>&1 || { echo >&2 "Python-virtualenv 3 needed: check your distro for installation guide."; exit 1; }
#
#
if [ -e venv ]
then
    echo "venv folder already exists..."
    echo "creating a new one? y or whatever..."
    read ANSWER
    case "$ANSWER" in
        YES | yes | Y | y | yep | YEP | yup | YUP) rm -rf venv/ && $VENV ;;
        *) echo "aborting..."; exit;;
    esac
else
    echo "creating venv folder..."
    $VENV
fi

echo "enter the v(irtual)environ"
source venv/bin/activate
# Install library and framework in virtual environment
pip3 install -r requirements.txt
echo "back to normality?"
read ANSWER2
case "$ANSWER2" in
    YES | yes | Y | y | yep | YEP | yup | YUP) deactivate;;
    *) echo "Welcome to your developing venv: HAPPY CODING!"; exit;;
esac

