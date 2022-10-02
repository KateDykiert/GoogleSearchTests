# GoogleSearchTests

## Table of contents
* [General information](#general-information)
* [Technologies](#technologies)
* [Setup](#setup)
* [Issues](#issues)

### General information
This project is a testing some sample functionalities of the Google search engine website.

### Technologies
* Python 3.8.10
* Selenium 4.5.0

### Setup
Install the latest version of Python.
https://www.python.org/downloads/

Make sure you have pip installed
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Download the requirements.txt
Then install the requirements listed in the requirements.txt using below
```
pip install -r /path/to/requirements.txt
```

### Issues
There is an issue sometimes when using find_element method that it only works with absolute XPaths given. This should be fixed because it may cause an issue if the DOM structure of the site where ever to be changed.
