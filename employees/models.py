from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=40)
    date_of_employment = models.DateField("Employment Date")
    department = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    salary = models.IntegerField()
    working_history = models.CharField(max_length=5000)
    employment_position = models.CharField(max_length=40)
    day_offs = models.IntegerField()
    personal_number = models.CharField(max_length=11)
    email = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=13)
    image = models.ImageField(upload_to="profile_image", blank=True)
    pension_fund = models.BooleanField(default=True)

    def __str__(self):
        return self.employee.name



