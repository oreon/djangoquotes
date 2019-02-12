# djangoquotes
DB related changes:
    sudo -u postgres psql
    create database blog;
    CREATE USER blog WITH PASSWORD 'blog';
    ALTER ROLE blog SET client_encoding TO 'utf8';
    alter role blog SET default_transaction_isolation TO 'read committed';
    alter role blog set timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE blog to blog;

Virtual environment related (can be done in the beginning as well):

    virtualenv quotes (to create a virtual env named aid4)
    source quotes/bin/activate (for quotes - source quotes/bin/activate)

Only after you are in the virtual environment do all the pip install stuff

    pip install -r requirements.txt
    pip install django gunicorn psycopg2-binary
    
Change Allowed_Hosts in mysite/settings.py if needed.

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
