from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Timetoread(models.Model):
    hours = models.IntegerField(default=0)
    mins = models.IntegerField(default=0)
    secs = models.IntegerField(default=0)

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=250)
    description = models.TextField(blank=True)
    body = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False)
    timetoreads=models.OneToOneField(Timetoread, on_delete=models.CASCADE, null=True)
    tags = TaggableManager(blank=True)

    def __int__(self):
        return self.id



