from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, template_name="home.html")

def ficha_page(request):
    return render(request, "ficha_list.html")