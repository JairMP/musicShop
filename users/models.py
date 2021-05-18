from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import OneToOneField

class User(AbstractUser):

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


