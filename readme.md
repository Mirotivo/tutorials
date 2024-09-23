1. Project Setup & Development
```shell
python -m django startproject tutorials
```
```shell
python manage.py startapp courses
```
```shell
python manage.py runserver
```

2. Database Migrations
```shell
python manage.py makemigrations
python manage.py migrate

```
```shell
python manage.py shell
```
```python
from courses.models import Course
Course.objects.create(title="Django Basics", description="Learn the basics of Django.")
```
```shell
python manage.py dbshell
```
```sql
INSERT INTO courses_course (title, description) VALUES ('Django Basics', 'Learn the basics of Django.');
```

3. User & Permissions Management
```shell
python manage.py createsuperuser
```
```shell
python manage.py changepassword ...
```

4. Project Deployment
```
python -m pip freeze > requirements.txt
docker run -p 8000:80 django-tutorials
```