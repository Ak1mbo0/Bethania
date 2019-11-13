from django.shortcuts import render
from upload.models import Ficha
from django.db.models import Q
# Create your views here.


def query(request):
    if 'search' in request.GET:
        search_term = request.GET['search']
        ficha = Ficha.objects.filter(Q(Titulo__icontains=search_term) | Q(Tema__icontains=search_term))
        return render(request, 'query.html', {
            "fichas": ficha,
            'search_term': search_term
        })
    else:
        return render(request, 'query.html')


