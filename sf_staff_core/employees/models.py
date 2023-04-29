from django.db import models


# Simple model for employees
class Employee(models.Model):

    name = models.TextField(max_length=50)
    surname = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    is_active = models.BooleanField(default=True)
    manager = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    is_manager = models.BooleanField(default=False)

