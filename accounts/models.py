from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class Meta(object):
        unique_together = ('email',)

    date_of_birth = models.DateField(null=True, blank=True)
    GENDERS = (
        ('m', 'male'),
        ('w', 'female'),
        ('o', 'other'),
    )
    gender = models.CharField(max_length=1, choices=GENDERS, default='o')
