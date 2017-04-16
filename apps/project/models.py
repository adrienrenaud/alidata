from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200, null=True)
    
    
class Chapter(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200, null=True)
    project = models.ForeignKey(Project)

    
class Notebook(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200, null=True)
    project = models.ForeignKey(Project)