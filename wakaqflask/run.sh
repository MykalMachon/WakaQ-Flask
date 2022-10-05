cd /app/

python3 /usr/local/bin/wakaq-worker --app='wakaqflask.tasks.wakaq' &
gunicorn --workers=3 --timeout=360 --bind=0.0.0.0:5000 'wakaqflask.app:create_flask()'
