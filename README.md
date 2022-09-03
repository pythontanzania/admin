# Pycon Tanzania Website API

This is the backend of the [Pycon Tanzania Website](pycon.or.tz). It is a collection of API endpoints created with the [Django Rest Framework](https://www.django-rest-framework.org).

It has three main apps:

 - Accounts - to manage user accounts
- Speakers - to manage speakers of the Pycon events
 - Events - to manage events and timetables

## Installation
First clone the repository:
```bash
git clone https://github.com/pycontanzania/admin pycon-admin

cd pycon-admin
```

Use [pip](https://pip.pypa.io/en/stable/) to install dependencies from 'requirements.txt':

```bash
pip install -r requirements.txt
```

## Usage
First migrate the database with:

```bash
python manage.py makemigrations

python manage.py migrate
```

Note that you might have to make migrations for each individual app as follows:

```bash
python manage.py makemigrations accounts

python manage.py makemigrations eventTimeTable

python manage.py makemigrations speakers
```
Create a super user account with:
```bash
python manage.py createsuperuser
```

Fill in the required details and run the app with:
```bash
python manage.py runserver
```
Access the site at: **127.0.0.1:8000**

## API Endpoints

The app consists of the following endpoints:

 - /admin - Django's default administrative portal. Requires authentication.

 - /api/events/ - To get a json response of all available events. Does not require authentication.

 - /api/events/{id} - To retrieve, update or delete individual event. Requires authentication.

 - /api/events/create/ - To create a new event. Requires authentication.

 - /api/speakers/ - To retrieve all speakers. Does not require authentication.

 - /api/speakers/{id} - To retrieve, edit or delete individual speaker. Requires authentication.

- /api/speakers/create/ - To create a new speaker. Does not require authentication.

 - /api/docs - To access Swagger UI documentation of the app.
 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
