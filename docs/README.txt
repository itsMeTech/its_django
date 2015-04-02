= Run the project on your local machine =

== execute migrations ==
python manage.py makemigrations
python manage.py migrate

== create an account ==
python manage.py createsuperuser

== run all test_data fixtures (optional) ==
python manage.py loaddata test_data

== run specific test_data fixture (optional) ==
python manage.py loaddata my_profile/fixtures/test_data

== run the project ==
python manage.py runserver
Point your browser to: http://127.0.0.1:8000/admin/
