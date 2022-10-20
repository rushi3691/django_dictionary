from django.db import models

class Word(models.Model):
    eng = models.CharField(max_length=200)
    mar = models.CharField(max_length=200)