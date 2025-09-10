from django.db import models;


class User(models.Model):
    nom = models.CharField(max_length=100)
    

