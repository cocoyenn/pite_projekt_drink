# pite_projekt_drink
Project for Python In The Enterprise course

# HOW TO RUN

--ENVIROMENT
1. Install pip
2. Install django via pip install django

--APPLICATION
1. Clone the repository
2. Enter to the app so u see manage.py
3. Run server in console by running command: python manage.py runserver
4. Server has started, monitored in the console, to stop, type Ctrl+C
5. Go to localhost:8000/app to see the application
6. localhost:8000/admin to admin panel

--TEST

1. If you want to run django tests:
```sh
$ python manage.py test app
```
--COVERAGE
1. Instalation: coverage via pip:
```sh
sudo pip install coverage
```
2. Run test with coverage:
```sh
$ coverage run --source='.' manage.py test app
```
And to see coverage statistics use: 
```sh
$ coverage report
```
If you want to see statistics as html:
```sh
$ coverage html
```