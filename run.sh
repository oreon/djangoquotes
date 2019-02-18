git pull
virtualenv -p python3.7 dquotes
source dquotes/bin/activate
pip install -r requirements.txt  # all requirements - gunicorn djang$
pip install gunicorn psycopg2-binary

python src/manage.py migrate
python src/manage.py collectstatic --noinput
sudo systemctl restart dquotes
deactivate