from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField(unique=True)
    address=models.TextField()
    fathers_name=models.CharField(default="",max_length=50)
    mothers_name=models.CharField(default="",max_length=50)
    

    def __str__(self):
        return f'Roll: {self.roll} | and  Name: { self.name}'