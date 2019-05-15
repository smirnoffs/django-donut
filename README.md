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

Swagger UI http://127.0.0.1:8000/docs/books/

Open API http://127.0.0.1:8000/swagger/books/?format=openapi

Browsable API http://127.0.0.1:8000/

## Run tests

Tests should be run from the django-donut/donut folder

```
pytest .
```



