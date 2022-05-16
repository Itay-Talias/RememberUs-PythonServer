# RememberUs-PythonServer

## Virtual Environment

### Creation

1.Check your Python version

```
$ python3 --version
```

In root folder (ea_server)

```
$ python3 -m venv virtualenv
```

### Activation

Activate the virtualenv (OS X & Linux)

```
$ source virtualenv/bin/activate
```

Activate the virtualenv (Windows)

```
$ virtualenv\Scripts\activate
```

### Package management

Install virtualenv set of dependencies:

```
$ pip install -r requirements.txt
```

Record virtualenv dependencies:

```
$ pip freeze > requirements.txt
```

Install new package (using the virtualenv pip):

```
$ virtualenv/bin/pip install {package name}
```

## Run

### Flask server

```
$ cd ea_server
$ export FLASK_APP=api
$ export FLASK_ENV=development
$ flask run
```

### Tests
