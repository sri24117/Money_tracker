from django.db import models
from django.contrib.auth.models import User
class User(models.Model):
    name = models.CharField(max_length=255)

class Transaction(models.Model):
    users = models.ManyToManyField(User)
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2