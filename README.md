# NBA Project - NBA Game Session Manager API

This is an application developed to manage NBA Game Sessions.

## Environment Setup

### Pre-requisites

1. Install Python v3.10
2. Install and Activate the virtual environment dedicated for the API

```commandline
python3 -m venv env
source env/bin/activate
```

3. Install dependencies from requirements.txt

```commandline
pip3 install -r requirements.txt
```

### Database

Execute from root directory of the project to make migrations and migrate schemas

```commandline
python3 manage.py makemigrations
python3 manage.py migrate
```

### Populate Data

Execute from root directory of the project to push dummy data into the database

```commandline
python3 manage.py loaddata NBA_API/fixtures/*
```

## Run the Application

Execute from the root directory to start the server

```commandline
python3 manage.py runserver
```

BasicAuth details of sample dummy users

```
Admin 
- username : admin1
- password : password123

Coach 
- username : coach1
- password : password123

Player
- username : player1
- password : password123
```
