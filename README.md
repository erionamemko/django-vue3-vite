#BACKEND REQUIREMENTS:
 Python 3, PIP, and venv
 
 You don't need to install a full-fledged database management system to develop with Django.
 You can use an SQLite database which allows you to have a file-based database that doesn't require any special installation.
 
Once you have all the requirements 
# initialize a virtual env on it
python3 -m venv ./ or python -m venv ./
then activate the virtual environment : source ./bin/activate
if you have windows : cd Scripts then type ./activate

Once your env is active install django
pip install django

#You can create your models and then migrate your database and start the development server:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


if you want to create a new app type:
django-admin startproject <new-app> .
django
└── new-app
    ├── manage.py
    ├── requirements.txt
    └── backend
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
then create a catalog to organise your project:
python manage.py startapp catalog
on your setting.py add your app 'catalog'


