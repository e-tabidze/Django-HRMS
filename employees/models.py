from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=40)
    date_of_employment = models.DateTimeField("Employment Date")
    department = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    salary = models.IntegerField()
    working_history = models.CharField(max_length=5000)
    employment_position = models.CharField(max_length=40)
    day_offs = models.IntegerField()
    personal_number = models.IntegerField()
    email = models.CharField(max_length=40)
    mobile_number = models.IntegerField()
    image = models.ImageField(upload_to="profile_image", blank=True)



