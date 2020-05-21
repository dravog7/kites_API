# Kite Foundation API

Used to sent emails to registrants using sendgrid
## REQUIREMENTS

- python 3.7.3 or above

## GETTING STARTED

The project is a django project

- Download the source code
- install required python modules

    ```python3 -m pip install requirements.txt```

- set the required environment variables (change the sendgrid API key in .env)

    ```source .env```

- in mailApp/mails.py change the FROM_EMAIL to an email that was verified in sendgrid.

- migrate the databases

    ```python3 manage.py makemigrations```

    ```python3 manage.py migrate```
- run the development server by

    ```python3 manage.py runserver```
