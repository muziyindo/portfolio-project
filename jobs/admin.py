from django.contrib import admin

# Register your models here.

#added this, anytime you want your models i.e tables to show on the python admin interface, you gotta add them here
from .models import Job
admin.site.register(Job)
