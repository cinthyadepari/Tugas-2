from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    tanggal = models.DateField()
    title = models.TextField()
    deskripsi = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)