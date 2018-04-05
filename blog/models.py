from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=1000)
