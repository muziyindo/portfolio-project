from django.db import models

# Create your models here.
#added this whole code
class Job(models.Model):
    image = models.ImageField(upload_to="image/")
    summary = models.CharField(max_length=200)

    '''NB: anytime you make changes on a model such as renaming a field or so, you will need to makemigrations
       and then migrate'''
