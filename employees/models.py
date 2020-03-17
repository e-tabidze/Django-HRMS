from django.db import models
from django.db.models import F


class Employee(models.Model):
    name = models.CharField(max_length=40)
    date_of_employment = models.DateTimeField("Employment Date")
    department = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    image_url = models.CharField(max_length=2083)
    salary = models.IntegerField()
    working_history = models.CharField(max_length=5000)
    employment_position = models.CharField(max_length=40)
    day_offs = models.IntegerField()
    personal_number = models.IntegerField()
    email = models.CharField(max_length=40)
    mobile_number = models.IntegerField()



