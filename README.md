# Activité 1 - Python Avancé

### Create a Project
You must create a new folder with
`mkdir project_name`
Then entering that folder with 
`cd project_name`

### Create a virtual environment
When you start working on a Python project for the first time, create a virtual environment inside your project with
`python3 -m venv .venv`

### Activate the Virtual Environment
Activate the new virtual environment so that any Python command you run or package you install uses it with
`source .venv/bin/activate`

### Installation
After activating the environment, you can install packages in it with 
`pip install "fastapi[standard]"`

### Run it
After you add your script, you can run your program, and it will use the Python inside of your virtual environment with the packages you installed there with
`fastapi dev main.py`
