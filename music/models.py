from django.db import models

# Create your models here.
class Music(models.Model):
    name = models.CharField(max_length=1024)
    image = models.CharField(max_length=1024)
    audio = models.CharField(max_length=1024)
    desc = models.CharField("Description",max_length=999999)
    date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=1025)

    def __str__(self):
        return self.name