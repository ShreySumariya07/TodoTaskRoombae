from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=2000,unique=True)
    eta = models.DateField()
    complete = models.BooleanField(default=False)