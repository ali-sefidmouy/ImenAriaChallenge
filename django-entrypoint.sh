#!/usr/bin/env bash

python manage.py makemigrations
python manage.py migrate

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_USERNAME
fi

$@

echo "server running at port 8000"
echo "Author = $AUTHOR"
python manage.py runserver 0.0.0.0:8000
