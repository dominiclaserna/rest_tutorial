# How to setup?

## Windows
- Setup WSL: https://learn.microsoft.com/en-us/windows/wsl/install
- Install pyenv (look for installation guide for WSL): https://github.com/pyenv/pyenv?tab=readme-ov-file#installation
- Install python 3.11.3 using pyenv

## Mac OS
- Install pyenv (look for installation guide for MacOS): https://github.com/pyenv/pyenv?tab=readme-ov-file#installation
- Install python 3.11.3 using pyenv

## Cloning
- Use SSH to clone this repo
- After cloning, open your terminal and cd to this directory
- Create a python virtualenv: `pyenv virtualenv 3.11.3 restful_tutorial`
- Activate the virtualenv: `pyenv activate restful_tutorial`
- Install dependencies: `pip install -r requirements.text`

# How to run the Flask App
- In the same terminal, run this command: `python myapp.py`
- You should see this message:
```python
* Serving Flask app 'myapp'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:8888
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 592-965-967
```
- Open your browser, and type this url in the address bar `http://localhost:888`
- Congrats! Flask app is up and running

# How to Test?
- Simply run the command: `pytest tests/`

# Available APIS as of now
## Users: Resource for list of available users
- GET: http://localhost:8888/api/v1/users
- POST: http://localhost:8888/api/v1/users

## User: Resource for single user
- GET: http://localhost:8888/api/v1/user/<id>


