from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from biogs.models import Biog
from tags.models import Tag
from snippets.models import Snippet
from tree.models import Tree, Family
from django.utils.html import escape
from django.core.exceptions import ValidationError
from django.contrib import messages
# Create your views here.

def index(request):
    biogs = Biog.objects.all()
    return render(request, 'biogs/biog_home.html', {'biogs': biogs})

def biog(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    snippets = Snippet.objects.all()
    biog_snips = []
    for tag in biog_.tags.all():
        for snippet in snippets:
            if tag in snippet.tags.all():
                biog_snips.append(snippet)
    biog_people = []
    for family in biog_.families.all():
        for child in family.children.all():
            if child not in biog_people:
                biog_people.append(child)
        if family.husband not in biog_people:
            biog_people.append(family.husband)
        if family.wife not in biog_people:
            biog_people.append(family.wife)
    families = Family.objects.all()
    #tags = Tag.objects.all()
    locations = Tag.objects.filter(tag_type='loc')
    occupations = Tag.objects.filter(tag_type='occ')
    periods = Tag.objects.filter(tag_type='per')
    persons = Tag.objects.filter(tag_type='ppe')
    subjects = Tag.objects.filter(tag_type='sub')
    return render(request, 'biogs/biog.html', {'biog': biog_, 'biog_snips': biog_snips,'biog_people':biog_people,'families':families, 'locations':locations,'occupations':occupations,
    'periods':periods, 'persons':persons, 'subjects':subjects}) 

def new_biog(request):
    biog = Biog.objects.create(first_name=request.POST.get('new_biog_first_name', ''),
                        surname=request.POST.get('new_biog_surname', ''),
                        birth_year=request.POST.get('new_biog_birth_year', '')
                        )    
    try:
        biog.full_clean()
    except ValidationError:
        biog.delete()
        messages.add_message(request, messages.INFO,'blank fields are not allowed.')
        return HttpResponseRedirect(reverse('biogs')) 
    return HttpResponseRedirect(reverse('biogs')) 

def add_tags(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    for key, value in request.POST.iteritems():
        if key.startswith('tag_'):
            tag_id = int(value)
            actual_tag = Tag.objects.get(id=tag_id)
            biog_.tags.add(actual_tag)
    biog_.save()        
    return redirect('/biogs/%d/#tags' % (biog_.id,))

def add_snippets(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    for key, value in request.POST.iteritems():
        if key.startswith('snip_'):
            snip_id = int(value)
            actual_snip = Snippet.objects.get(id=snip_id)
            biog_.snippets.add(actual_snip)
    biog_.save()
    return redirect('/biogs/%d/#snippets' % (biog_.id))    

def add_people(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    for key, value in request.POST.iteritems():
        if key.startswith('tree_'):
            tree_id = int(value)
            actual_tree = Tree.objects.get(id=tree_id)
            biog_.tree_members.add(actual_tree)
    biog_.save()
    return redirect('/biogs/%d/#people' % (biog_.id))

def add_families(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    families = biog_.families.all()
    for family in families:
        biog_.families.remove(family)
    
    for key, value in request.POST.iteritems():
        if key.startswith('family_'):
            family_id = int(value)
            actual_family = Family.objects.get(id=family_id)
            if actual_family not in biog_.families.all():
                biog_.families.add(actual_family)
                
    biog_.save()
    return redirect('/biogs/%d/#people' % (biog_.id))

def remove_tags(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    #biog_.tags.all().clear()
    tags = biog_.tags.all()
    for tag in tags:
        biog_.tags.remove(tag)
    for key, value in request.POST.iteritems():
        if key.startswith('tag_'):
            tag_id = int(value)
            actual_tag = Tag.objects.get(id=tag_id)
            biog_.tags.add(actual_tag)
    biog_.save()
    return redirect('/biogs/%d/#tags' % (biog_.id,))

def remove_snippets(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    snippets = biog_.snippets.all()
    for snip in snippets:
        biog_.snippets.remove(snip)
    for key, value in request.POST.iteritems():
        if key.startswith('snip_'):
            snip_id = int(value)
            actual_snip = Snippet.objects.get(id=snip_id)
            biog_.snippets.add(actual_snip)
    biog_.save()
    return redirect('/biogs/%d/#snippets' % (biog_.id,))


def save_notes(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    biog_notes = request.POST.get('biog_notes', '')
    biog_.notes = biog_notes
    biog_.save()
    return redirect('/biogs/%d' % (biog_.id,)) 
