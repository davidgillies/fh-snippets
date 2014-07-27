from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        return render(request, 'biog_home.html', {'new_biog_first_name':request.POST.get('new_biog_first_name', ''),
                                                  'new_biog_surname':request.POST.get('new_biog_surname', ''),
                                                  'new_biog_birth_year':request.POST.get('new_biog_birth_year', ''),})
    return render(request, 'biog_home.html')
