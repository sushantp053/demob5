from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(auto_created=True, primary_key=True)
    city = models.CharField(max_length=50)
    marks = models.IntegerField()
    pass_year = models.IntegerField()
    mobile = models.IntegerField()
    email = models.CharField(max_length=50)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)
    hod = models.CharField(max_length=50)
    hod_mobile = models.IntegerField()
    hod_email = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.hod
