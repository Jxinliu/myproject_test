from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.

def homepage(request):
    templare = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = templare.render(locals())
    return HttpResponse(posts)