from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    department = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.department} - {self.age}"
