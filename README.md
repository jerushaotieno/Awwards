### Author
Jerusha Otieno

### Description
This application allows a user to post a project he/she has created and get it reviewed by his/her peers based on design, usability and content.

### User Story
A user of the application is able to:

* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View their profile page

### Getting Started
To set up the project in your local machine for development and testing:

1. Clone this Repository

git clone https://github.com/jerushaotieno/Awwards.git

2. Enable your Python development environment
Add Python, pip and a virtual environment to get started:

$ python3.6 -m venv --without-pip virtual

$ source virtual/bin/activate

(virtual) $ curl https://bootstrap.pypa.io/get-pip.py | python

### Prerequisites
Install all project requirements using the package manager pip.

(virtual) $ pip install -r requirements.txt

### Installation
* Use the .env.example file to create a .env file with appropriate values to get a development env running.
* Create a postgres db and add the credentials to .env file
* Apply initial migrations

    (virtual) $ python manage.py migrate

* Create admin account

    (virtual) $ python manage.py createsuperuser

* Make migrations to your database

    (virtual) $ python manage.py makemigrations (app name)

    (virtual) $ python manage.py migrate

* Start development server

    (virtual) $ python3 manage.py runserver

### Running Tests
To run automated tests for the system:

(virtual) $ python3 manage.py test (app name)

### Deployment
With all environment variables changed to suit your local copy of this repository, deploy the application to Heroku to see it live or simply run it locally

(virtual) $ python3 manage.py runserver

### Technology Used
* Django 3.0.8 - The web framework used 
* Heroku - Deployment platform 
* Python3 - Backend logic 
* Postresql - Database system

### Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

### Contact Information
If you have any question or contributions, please email: jerushaotienocoding@gmail.com

### License
MIT License

### Copyright
Copyright (c) 2022 Jerusha Otieno