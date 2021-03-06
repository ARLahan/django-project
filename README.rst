====================================================
django-project
====================================================

Based on 'django-twoscoops-project'

A project template adjusted for:

- Python 3.4
- Django 1.7
- Jinja2 templating system
- django-ckeditor


To use this project follow these steps:

#. Create your working environment
#. Install Django
#. Create the new project using this template
#. Install additional dependencies

*note: these instructions show creation of a project called "icecream".  You
should replace this name with the actual name of your project.*


Working Environment
===================
Create a virtual working environment::

    $ pyvenv icecream

This will install a Python 3.4 environment in the current location (e.g. /home/user/...).

You will also need to ensure that the pyvenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.


Installing Django
=================

To install Django in the new virtual environment, run the following command::

    $ pip install django
    

Creating your project
=====================

To create a new Django project called '**icecream**' using
this **django-project**, run the following command::

    $ django-admin.py startproject --template=https://github.com/LahanAR/django-project/archive/master.zip --extension=py,rst,html icecream


Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/dev.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Based on
======================

This project follows some of the best practices as espoused in `Two Scoops of Django: Best Practices for Django 1.6`_.

.. _`Two Scoops of Django: Best Practices for Django 1.6`: http://twoscoopspress.org/products/two-scoops-of-django-1-6