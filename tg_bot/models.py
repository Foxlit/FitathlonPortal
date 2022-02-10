from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=100)
