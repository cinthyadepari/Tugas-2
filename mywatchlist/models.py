from random import choices
from django.db import models

class ModelMyWatchList(models.Model):
    watched = models.CharField(max_length= 6)
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
