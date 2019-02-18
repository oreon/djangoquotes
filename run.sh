git pull
virtualenv -p python3.7 dquotes
source dquotes/bin/activate
pip install -r requirements.txt  # all requirements - gunicorn djang$
pip install gunicorn psycopg2-binary

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py installtasks
sudo systemctl restart dquotes
deactivate