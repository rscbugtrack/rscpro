# RSC Projects

* Python 2 or Python 3
* Django 1.11
* PostgreSQL or MySQL

## Setting Up for Development

These are instructions for setting up healthchecks Django app
in development environment.



* prepare virtual environment
  (with virtualenv you get pip, we'll use it soon to install requirements):
        $ sudo apt-get install python3-dev

        $ virtualenv --python=python3 rsc-venv

        $ source rsc-venv/bin/activate

* check out project code:

        $ https://github.com/rscbugtrack/rscpro.git

* install requirements (Django, ...) into virtualenv:

        $ pip install -r rscpro/requirements.txt

* healthchecks is configured to use a SQLite database by default. To use
  PostgreSQL or MySQL database, create and edit `hc/local_settings.py` file.
  There is a template you can copy and edit as needed:

        $ cd ~/rscpro
        $ cp hc/local_settings.py.example hc/local_settings.py

* create database tables and the superuser account:

        $ cd ~/rscpro
        $ ./manage.py migrate
        $ ./manage.py createsuperuser

* run development server:

        $ ./manage.py runserver

The site should now be running at `http://localhost:8080`
To log into Django administration site as a super user,
visit `http://localhost:8080/admin`






