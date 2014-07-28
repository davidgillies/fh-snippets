from django.shortcuts import redirect, render
from django.http import HttpResponse
from biogs.models import Biog

# Create your views here.

def index(request):
    if request.method == 'POST':
        biog = Biog()
        biog.first_name = request.POST.get('new_biog_first_name', '')
        biog.surname = request.POST.get('new_biog_surname', '')
        biog.birth_year = request.POST.get('new_biog_birth_year', '')
        biog.save()
        return redirect('/biogs')

    biogs = Biog.objects.all()
    return render(request, 'biog_home.html', {'biogs': biogs})
