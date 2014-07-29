from django.shortcuts import redirect, render
from django.http import HttpResponse
from biogs.models import Biog

# Create your views here.

def index(request):
    biogs = Biog.objects.all()
    return render(request, 'biog_home.html', {'biogs': biogs})

def biog(request):
    biogs=Biog.objects.all()
    return render(request, 'biog.html', {'biogs': biogs}) 

def new_biog(request):
    Biog.objects.create(first_name=request.POST.get('new_biog_first_name', ''),
                        surname=request.POST.get('new_biog_surname', ''),
                        birth_year=request.POST.get('new_biog_birth_year', '')
                        )    
    return redirect('/biogs')