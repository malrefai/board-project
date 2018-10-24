[![Build Status](https://travis-ci.org/malrefai/board-project.svg?branch=develop)](https://travis-ci.org/malrefai/board-project)
[![codecov](https://codecov.io/gh/malrefai/board-project/branch/develop/graph/badge.svg)](https://codecov.io/gh/malrefai/board-project)

# Board App
Board app is a ...

**Board app** built with [Python][0]

## Technology Stack

- [Python][0]
- [Django][1]
- [Django REST framework][2]

## Installation Guide

### 1. Install [Python 3.7.*][3]

    # https://www.python.org/downloads/

### 2. Install virtualenv

	$ pip install virtualenv
	
### 3. Setup virtualenv

	# Create and activate virtual env
	$ virtualenv <ENV_DIR>
	$ source <ENV_DIR>/bin/activate
	
### 4. Fork the repository

    # Fork repository to your github account

### 5. Clone the repository

    # Create a project directory 
	# Clone board-project repository into project directory
    $ git clone git@github.com:<GITHUB_ACCOUNT>/board-project.git <YOUR_PROJECT_DIR>
    $ cd <YOUR_PROJECT_DIR>

### 6. Install dependencies

On the project root there is a requirements.txt file. 

Make sure you install all the required dependencies before running todo app

    $ pip install -r requirements/development.txt
    
### 7. Add .env file

Create .env file

    $ vim .env
    
Write the following:

    ##
    # Environment
    ##
    ENV="development"

    ##
    # Secret Key
    ##
    SECRET_KEY="PUT_YOUR_SECRET_KEY_HERE"

### 8. Demo

    $ python manage.py runserver

## Copyright

Copyright (c) 2018 Mohammad Alrefai. See LICENSE.txt for further details.

## License

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: http://www.django-rest-framework.org/
[3]: https://www.python.org/downloads/

