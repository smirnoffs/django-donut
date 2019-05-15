#Setup the virtual environment

```bash
cd django-donut
python3 -m venv .env
source .env/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Apply database migrations

```
cd donut
python manage.py migrate
```

## Start the server 

```
python manage.py runserver
```

## Run tests

Tests should be run from the django-donut/donut folder

```
pytest .
```

