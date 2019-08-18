from django.db import models

# Create your models here.
#added this whole code
class Blog(models.Model):
	title = models.CharField(max_length=300)
	pub_date = models.DateField(auto_now=False, auto_now_add=False) #models.DateTime
	body = models.TextField(max_length=1000)
	image = models.ImageField(upload_to="image/blogimages/")

	'''NB: anytime you make changes on a model such as renaming a field or so, you will need to makemigrations
       and then migrate'''