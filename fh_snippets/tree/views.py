from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from tree.forms import UploadFileForm
from tree.utilities.gedcom_parser import handle_uploaded_file, import_gedcom_data
from django.template import RequestContext

def index(request):
    return HttpResponse('')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['filename'])
            import_gedcom_data()
            return HttpResponseRedirect('/tree')
    else:
        form = UploadFileForm()
    
    return render(request,'tree/upload.html', {'form':form})

