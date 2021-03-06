# project overview

A simple Flask web server application that (optionally) runs on
Heroku. This web application was built as a project for the Udacity Full Stack Nanodegree program.
Some notable parts used in this web application are:

  1. [Flask](http://flask.pocoo.org/)
  2. [Gunicorn](http://gunicorn.org/)
  3. [Flask-Restless](https://flask-restless.readthedocs.org/en/latest/)
  4. [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/)
  5. [Flask-Bootstrap](http://pythonhosted.org/Flask-Bootstrap/)
  6. [Flask-Script](http://flask-script.readthedocs.org/en/latest/)


### setup a virtualenv

Create a virtual environment the web application by running the following
commands in a terminal.

```bash
pip install -r requirements.txt
python setup.py develop
```

### start the web server

Before you start the web server you should prime the database with a few sample
entries.

```bash
./manage.py prime_database
```

Then, start the web server on your local machine using Flask-Manager.

```bash
./manage.py runserver
```
