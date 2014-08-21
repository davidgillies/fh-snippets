from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from tags.models import Tag
from biogs.models import Biog
from rest_framework import viewsets, generics
from tags.serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
   
class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagsIndex(ListView):
    #model = Tag
    queryset = Tag.objects.order_by('tagname')
    context_object_name = 'tag_list'
    # template_name = "tags/tagdsfsdafas_list.html"    

class TagsDetailView(DetailView):
    context_object_name = 'tag_list'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagsDetailView, self).get_context_data(**kwargs)
        context['biog_list'] = Biog.objects.all()
        return context
