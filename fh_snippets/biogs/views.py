from django.shortcuts import redirect, render
from django.http import HttpResponse
from biogs.models import Biog
from tags.models import Tag
from snippets.models import Snippet
from tree.models import Tree 

# Create your views here.

def index(request):
    biogs = Biog.objects.all()
    return render(request, 'biog_home.html', {'biogs': biogs})

def biog(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    snippets = Snippet.objects.all()
    biog_snips = []
    for tag in biog_.tags.all():
        for snippet in snippets:
            if tag in snippet.tags.all():
                biog_snips.append(snippet)
    tags = Tag.objects.all()
    return render(request, 'biog.html', {'biog': biog_, 'tags':tags, 'biog_snips': biog_snips,}) 

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

def add_snippets(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    for key, value in request.POST.iteritems():
        if key.startswith('snip_'):
            snip_id = int(value)
            actual_snip = Snippet.objects.get(id=snip_id)
            biog_.snippets.add(actual_snip)
    biog_.save()
    return redirect('/biogs/%d' % (biog_.id))    
