"""
Database models.
"""
from django.db import models


class Designation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
