from django.db import models

# Create your models here.
#added this whole code
class Blog(models.Model):
	title = models.CharField(max_length=300)
	pub_date = models.DateField(auto_now=False, auto_now_add=False) #models.DateTime
	body = models.TextField(max_length=1000)
	image = models.ImageField(upload_to="image/blogimages/")

	#returns specified text chunk from body
	#nb: when you define a functon in a class you must pass a self parameter into it
	def summary(self):
		return self.body[:100] #extract first 100 characters

	def __str__(self):
		return self.title #show titles in python admin page for blog model


	'''NB: anytime you make changes on a model such as renaming a field or so, you will need to makemigrations
       and then migrate'''