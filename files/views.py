from django.shortcuts import render

# Create your views here.

def files_page(request):
    return render(request, template_name="files.html")
