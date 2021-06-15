from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse


def index(request):
    posts = Blogpost.objects.all()  # sending the blogpost to index.html by fetchong it from databse.
    return render(request, 'blog/index.html', {'posts': posts})


def blogpost(request, id):
    Posts = Blogpost.objects.filter(post_id = id)[0]  # sending the blogpost to index.html by fetchong it from databse.
    print(Posts)
    return render(request, 'blog/blogpost.html', {'Posts': Posts})

