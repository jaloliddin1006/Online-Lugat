from django.db import models

# Create your models here.
class Lugat(models.Model):
    eng = models.CharField('Inglizcha', max_length=128)
    uzb = models.CharField("O'zbekcha", max_length=128)