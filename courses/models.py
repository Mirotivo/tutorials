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

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    tutor = models.ForeignKey(Profile, related_name='taught_courses', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def assign_tutor(self, profile):
        if profile.is_tutor():
            self.tutor = profile
        else:
            raise ValueError("Assigned tutor must have the tutor role.")

class Chat(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}: {self.message}"
