from django.shortcuts import render

# Create your views here.

def contatos_page(request):
    return render(request, template_name="contatos.html")
