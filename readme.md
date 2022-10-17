### This is the starting point of a Django4 app. It is a django Sample App source code

## I have followed this video to develop this django project
    https://www.youtube.com/watch?v=ey8EXTjRuag

## Following commands were run on Git Bash for starting this Django project
    mkdir djangoSampleApp
    cd djangoSampleApp/
    git init
    python -m venv virt
    source virt/Scripts/activate
    pip install django
    pip freeze
    django-admin startproject mysite
    cd mysite/
    python manage.py migrate
    python manage.py runserver

# Ctrl + c to stop or break out of the server

## After these an admin user and password needs to be created
    winpty python manage.py createsuperuser
    python manage.py startapp websiteUPI
    python manage.py runserver
