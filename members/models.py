from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=255)
    activation_date = models.DateTimeField(blank=False)
    deactivation_date = models.DateTimeField(blank=True, null=True)
    department = models.CharField(max_length=64, blank=True)
    designation = models.CharField(max_length=64, blank=True)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)