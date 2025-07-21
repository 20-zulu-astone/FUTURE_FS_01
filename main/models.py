from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


# Create your models here.
