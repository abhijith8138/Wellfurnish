from django.db import models

# Create your models here.
class Sofa(models.Model):
    name = models.CharField(max_length=5000)
    about = models.CharField(max_length=5000)
    image =  models.CharField(max_length=5000)
    def __str__(self) -> str:
        return self.name
class Blinds(models.Model):
    name = models.CharField(max_length=5000)
    about = models.CharField(max_length=5000)
    image =  models.CharField(max_length=5000)
    def __str__(self) -> str:
        return self.name
class Bed(models.Model):
    name = models.CharField(max_length=1000)
    about = models.CharField(max_length=5000)
    image =  models.CharField(max_length=5000)
    def __str__(self) -> str:
        return self.name
class Curtains(models.Model):
    name = models.CharField(max_length=5000)
    about = models.CharField(max_length=5000)
    image =  models.CharField(max_length=5000)
    def __str__(self) -> str:
        return self.name
class Doorlock(models.Model):
    name = models.CharField(max_length=5000)
    about = models.CharField(max_length=5000)
    image =  models.CharField(max_length=5000)
    def __str__(self) -> str:
        return self.name