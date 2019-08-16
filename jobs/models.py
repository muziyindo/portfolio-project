from django.db import models

# Create your models here.
#added this whole code
class Job(models.Model):
    image = models.Image(uploaded_to="")
    summary = models.CharField(max_length=200)
