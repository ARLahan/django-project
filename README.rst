====================================================
django-project
====================================================

Based on 'django-twoscoops-project'

A project template adjusted for:

- Python 3.4
- Django 1.7 and
- Jinja2 templating system


To use this project follow these steps:

#. Create your working environment
#. Install Django
#. Create the new project using the django-two-scoops template
#. Install additional dependencies

*note: these instructions show creation of a project called "icecream".  You
should replace this name with the actual name of your project.*


Working Environment
===================
Create a virtual working environment::

    $ pyvenv icecream

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.


Installing Django
=================

To install Django in the new virtual environment, run the following command::

    $ pip install django
    

Creating your project
=====================

To create a new Django project called '**icecream_project**' using
django-twoscoops-project, run the following command::

    $ django-admin.py startproject --template=https://github.com/LahanAR/django-project/archive/master.zip --extension=py,rst,html icecream_project


Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/env.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Follows Best Practices
======================

.. image:: http://twoscoops.smugmug.com/Two-Scoops-Press-Media-Kit/i-C8s5jkn/0/O/favicon-152.png
   :name: Two Scoops Logo
   :align: center
   :alt: Two Scoops of Django
   :target: http://twoscoopspress.org/products/two-scoops-of-django-1-6

This project follows best practices as espoused in `Two Scoops of Django: Best Practices for Django 1.6`_.

.. _`Two Scoops of Django: Best Practices for Django 1.6`: http://twoscoopspress.org/products/two-scoops-of-django-1-6

Acknowledgements
================

- Many thanks to Randall Degges for the inspiration to write the book and django-skel.
- All of the contributors_ to this project.

.. _contributors: https://github.com/twoscoops/django-twoscoops-project/blob/master/CONTRIBUTORS.txt
