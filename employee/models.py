from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.name} - {self.age}"

