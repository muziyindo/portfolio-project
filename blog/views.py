from django.shortcuts import render
from django.shortcuts import get_object_or_404 # used to get data from the db or return 404 if data is not found
from .models import Blog

# Create your views here.

def allBlogs(request):
	posts = Blog.objects
	return render(request,'blog/allblogs.html',{'posts':posts})

def detail(request,blog_id):
	detailblog = get_object_or_404(Blog, pk=blog_id)
	return render(request,'blog/detail.html',{'detail':detailblog})