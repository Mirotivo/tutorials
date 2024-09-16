```
python -m django startproject tutorials
```
```
python -m pip freeze > requirements.txt
cd tutorials
python manage.py startapp courses
```
```
python manage.py makemigrations
python manage.py migrate

```
```
python manage.py shell
from courses.models import Course
Course.objects.create(title="Django Basics", description="Learn the basics of Django.")
```
```
python manage.py runserver
docker run -p 8000:80 django-tutorials
```