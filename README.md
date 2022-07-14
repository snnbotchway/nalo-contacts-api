# Nalo-Contact-Management-Api with Django Rest Framework
This RESTful API helps to keep and manage customer phone number address books.

## Requirements
- Django 4.0.6
- djangorestframework 3.13.1
- psycopg2 2.9.3
- django-dotenv 1.4.2

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command

`pip install pipenv`, then

For python3:
`pipenv --three`

For python2:
`pipenv --two`

You can install all the required dependencies by running
`pipenv install -r requirements.txt`

After this, it is necessary to activate the virtual environment
`pipenv shell`

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, and DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `api`, so we will use the following URLs - `/api/` and `/api/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api` | GET | READ | Get all contacts(20 per page)
`api/:id` | GET | READ | Get a single contact
`api/contact-create`| POST | CREATE | Create a new contact
`api/contact-edit/:id` | PUT | UPDATE | Update a contact
`api/contact-delete/:id` | DELETE | DELETE | Delete a contact
`api/upload-csv` | POST | CREATE | Upload a csv file to create contacts and send email to user who uploads csv data successfully

## Setting Up Postgresql
- To proceed, install postgresql from https://www.postgresql.org/download/
- Run pgAdmin and connect to one server. You can use a local server or create a remote one on https://www.elephantsql.com/
- Right-click the server, click properties and note down the connection details. If you used the remote server, get the connection details from elephantsql.
- Create a database as well.

## Gmail Config
To enable automated mail sending in Django, we are required to set up a google account to do so.
- Login to the google account you wish to use to send the emails.
- At https://myaccount.google.com/security, configure Two-Factor-Authentication and turn it on.
- Just below, click `App Passwords` and generate a password for SMTP. Note this password as it will be used later.
- At https://accounts.google.com/b/0/DisplayUnlockCaptcha, grant access to the account.

## Setting Environment Variables
Create a `.env` file in the same directory as `manage.py`
Set the following variables using information from your own Gmail and your PostgreSQL server. It should look like this:
```
DATABASE_NAME='postgres'
DATABASE_USER='postgres'
DATABASE_PASS='<Your postgresql master password or server password>'
DATABASE_HOST='localhost'
DATABASE_PORT='5432'
EMAIL_USER=<Your email address>
EMAIL_PASSWORD=<SMTP generated password>
SECRET_KEY = '<Contact solomonbotchway7@gmail.com for secret key>'
DEBUG=True
```

## Run Server

Run the following to create initial database tables:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

Only an admin can use this API so create one:

`python3 manage.py createsuperuser`

Give this user an email as the CSV file upload notification will be sent to it.

Run the makemigrations and migrate commands once more to add the user to the database.

Now `python3 manage.py runserver`

Open another terminal and test the API with the tests provided:

`python3 manage.py test`

All 5 endpoints should pass the test at this point

## Use
- Open a browser and enter the URL from the `python3 manage.py runserver` command

For example, if the URL is `http://127.0.0.1:8000/`:

- Go to `http://127.0.0.1:8000/admin/` and log in with the credentials of the superuser you created.
- You will now have access to all the endpoints
- Load initial data by uploading the `mock_data(10,000 entries).csv` in this repo to `http://127.0.0.1:8000/api/upload-csv/`. (Credit to mockaroo.com for the mock data) A notification will be sent to the admin's email upon the successful population of the database from the email we set up earlier.

List phone numbers/contacts in batches of 20 with pagination through the rest of the record)

`http://127.0.0.1:8000/api/contact-list` 

Create a new contact

`http://127.0.0.1:8000/api/contact-create`

Retrieve a contact with id

`http://127.0.0.1:8000/api/<id>`

Edit contact with id

`http://127.0.0.1:8000/api/contact-edit/<id>`

Delete contact with id

`http://127.0.0.1:8000/api/contact-delete/<id>`





