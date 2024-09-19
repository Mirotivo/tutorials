from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLE_STUDENT = 1  # 0001
    ROLE_TUTOR = 2    # 0010

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.IntegerField(default=0)

    def is_student(self):
        return self.roles & self.ROLE_STUDENT == self.ROLE_STUDENT

    def is_tutor(self):
        return self.roles & self.ROLE_TUTOR == self.ROLE_TUTOR

    def set_role(self, role):
        self.roles |= role

    def remove_role(self, role):
        self.roles &= ~role

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
