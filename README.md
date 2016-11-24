# DogAdoption-Backend
Building a Flask RESTful API to use in web and mobile apps and learning the framework.<br/>
The project is basically a platform to register abandoned dogs and allow interested people to adopt them.<br/>
Feel free to fork and help with the project. :)

### Quick guide to run

* First off, you need to clone the repository:
```
$ git clone https://github.com/gabrielecker/DogAdoption-Backend.git
$ cd DogAdoption-Backend
$ git checkout dev
```
* Then you need to create your virtual environment, <a href="https://virtualenvwrapper.readthedocs.io/en/latest/">virtualenvwrapper</a> is recommended:
```
$ mkvirtualenv DogAdoption
```
* Now we install some dependencies:
```
$ pip install -r requirements.txt
```
##### Create the database as you wish described in project.config.SQLALCHEMY_DATABASE_URI.<br/> Example: My development db url is 'postgresql://postgres:@localhost/dog_adoption' so 'dog_adoption' database must be created.
* Then we sync the database with our models:
```
$ ./manage.py db init
$ ./manage.py db migrate
$ ./manage.py db upgrade
```
* By this time everything should be fine so just type:
```
$ ./run.py
```
### License

This application is licensed under the MIT License. You are free to remix, adapt and redistribute it, however, please credit the original authors
