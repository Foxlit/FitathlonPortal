from django.db import models
import constants


class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    department = models.CharField(max_length=2, choices=constants.DEPARTMENTS)


class Component(models.Model):
    name = models.CharField(max_length=255)


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    component = models.CharField(Component, on_delete=models.RESTRICT)

