from django.shortcuts import redirect, render
from django.http import HttpResponse
from biogs.models import Biog

# Create your views here.

def index(request):
    biogs = Biog.objects.all()
    return render(request, 'biog_home.html', {'biogs': biogs})

def biog(request, biog_id):
    biog_ = Biog.objects.get(id=biog_id)
    #tags = Tag.objects.filter(biog=biog_)
    return render(request, 'biog.html', {'biog': biog_}) 

def new_biog(request):
    Biog.objects.create(first_name=request.POST.get('new_biog_first_name', ''),
                        surname=request.POST.get('new_biog_surname', ''),
                        birth_year=request.POST.get('new_biog_birth_year', '')
                        )    
    return redirect('/biogs')