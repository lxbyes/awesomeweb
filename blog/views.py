# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

from blog.models import BlogsPost

# Create your views here.

def index(request):
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html', {'posts': blog_list})