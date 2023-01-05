from django.db import models
# Create your models here.

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    tittle = models.CharField(max_length=32)
    content = models.CharField(max_length=2048) 

    def __unicode__(self):
        return self.message





