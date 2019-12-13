from django.shortcuts import render
from upload.models import Ficha, Video
from django.db.models import Q
# Create your views here.


def query(request):
    if 'search' in request.GET:
        search_term = request.GET['search']
        if 'document' == 'Ficha':
            ficha = Ficha.objects.filter(Q(Titulo__icontains=search_term) | Q(Tema__icontains=search_term))
            tipo = Ficha.Tipo
            return render(request, 'query.html', {
            "fichas": ficha,
            'search_term': search_term,
            'tipo': tipo,

            })
        elif 'document' == 'Video':
            video = Video.objects.filter(Q(Titulo__icontains=search_term) | Q(Tema__icontains=search_term))
            tipo = Video.Tipo
            return render(request, 'query.html', {
                "videos": video,
                'search_term': search_term,
                'tipo': tipo,

            })
    else:
        return render(request, 'query.html')


