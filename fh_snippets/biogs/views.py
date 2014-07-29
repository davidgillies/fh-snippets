from django.shortcuts import redirect, render
from django.http import HttpResponse
from biogs.models import Biog
from tags.models import Tag

# Create your views here.

def index(request):
    biogs = Biog.objects.all()
    return render(request, 'biog_home.html', {'biogs': biogs})

def biog(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    tags = Tag.objects.all()
    return render(request, 'biog.html', {'biog': biog_, 'tags':tags}) 

def new_biog(request):
    Biog.objects.create(first_name=request.POST.get('new_biog_first_name', ''),
                        surname=request.POST.get('new_biog_surname', ''),
                        birth_year=request.POST.get('new_biog_birth_year', '')
                        )    
    return redirect('/biogs')

def add_tags(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    for key, value in request.POST.iteritems():
        if key.startswith('tag_'):
            tag_id = int(value)
            actual_tag = Tag.objects.get(id=tag_id)
            biog_.tags.add(actual_tag)
    biog_.save()        
    return redirect('/biogs/%d' % (biog_.id,))
    