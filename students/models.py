from django.db import models

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=200,verbose_name='First Name')
    last_name=models.CharField(max_length=200,verbose_name="Last Name")
    email=models.EmailField(max_length=100)
    faculty=models.CharField(max_length=50, verbose_name="Faculty")
    gpa=models.FloatField(verbose_name="GPA")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'