from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=1000)
