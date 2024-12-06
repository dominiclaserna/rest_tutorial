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

## Setting up dependencies
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
- GET: http://localhost:8888/api/v1/users (type this to your browser address bar and see the magic!)
- POST: http://localhost:8888/api/v1/users
- Sample post command using cURL, you can try hitting it:
  ```curl
  curl -X POST https://localhost:8888/api/v1/users \
   -d '{"firstname": "kimi", "lastname": "no nawa"}'  
  ```
- Now, try using the GET method again to inspect if the new user data has been inserted.


## User: Resource for single user
- GET: http://localhost:8888/api/v1/user/<id>


# Disclaimer
- We're not using any database. Hence, data will always be lost after restarting the server.

