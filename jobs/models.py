from django.db import models

# Create your models here.
#added this whole code
class Job(models.Model):
    project_title = models.CharField(max_length=500,null=True)
    project_description = models.TextField(max_length=1000,null=True)
    image = models.ImageField(upload_to="image/")
    

    '''NB: anytime you make changes on a model such as renaming a field or so, you will need to makemigrations
       and then migrate'''
