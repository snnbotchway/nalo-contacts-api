# Nalo-Contact-Management-Api with Django Rest Framework
This RESTful API helps to keep and manage customer phone number address books.

## Requirements
- Django 4.0.6
- djangorestframework 3.13.1
- psycopg2 2.9.3

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command

For python3:
```
pipenv --three
```
For python2:
```
pipenv --two
```
After this, it is necessary to activate the virtual environment
```
pipenv shell
```

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, and DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `api`, so we will use the following URLS - `/api/` and `/api/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api` | GET | READ | Get all contacts(20 per page)
`api/:id` | GET | READ | Get a single contact
`api/contact-create`| POST | CREATE | Create a new contact
`api/:id` | PUT | UPDATE | Update a contact
`api/:id` | DELETE | DELETE | Delete a contact
`api/upload-csv` | POST | CREATE | Upload a csv file to create contacts and send email to user who uploads csv data successfully



