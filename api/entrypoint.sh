#!/bin/sh


echo "Waiting for postgres..."
while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
  sleep 0.2
done
echo "PostgreSQL started"

# dockerfile sets workdir to api_home
#python manage.py flush --no-input  # this script always runs, even if the database already exists
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"
