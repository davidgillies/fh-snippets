from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from tags.models import Tag

#def index(request):
#    return HttpResponse('')

class TagsIndex(ListView):
    model = Tag

