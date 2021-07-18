from django.db import models
from django.shortcuts import render

# Create your models here.
class Scrap(models.Model) :
    title = models.CharField(max_length=30)
    author = models.CharField(null=True,default='',max_length=20)
    body = models.TextField()

    def __str__(self) :
        return self.title


    def summary(self) :
        return self.body[:150]
