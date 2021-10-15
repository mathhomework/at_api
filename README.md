# Adventure Time API

## Set up

1. Create a virtual environment: `python3 -m venv .venv`
1. Activate the virtual environment: `. ./.venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Set environment variables:
   ```
   export SECRET_KEY=dev
   export DEBUG=True
   export ALLOWED_HOSTS=127.0.0.1,localhost
   ```
1. Migrate the database: `python manage.py migrate`
1. Collect static files: `python manage.py collectstatic --noinput`
1. Run the dev server: `python manage.py runserver`
1. View the running application in a browser at http://localhost:8000

## Helpful Links

- [Python](https://www.python.org/)
- [Django](https://djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
