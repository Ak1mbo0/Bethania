from django.shortcuts import render
from upload.models import Ficha, Video
from django.db.models import Q
# Create your views here.


def query(request):
    if 'search' in request.GET:
        search_term = request.GET['search']
        search_filter = request.GET['Document']
        if search_filter == 'Ficha':
            ficha = Ficha.objects.filter(Q(Titulo__icontains=search_term) | Q(Tema__icontains=search_term))
            return render(request, 'query.html', {
                "fichas": ficha,
                'search_term': search_term,
                'search_filter': search_filter
            })
        elif search_filter == 'Video':
            video = Video.objects.filter(Q(Titulo__icontains=search_term) | Q(Tema__icontains=search_term))
            return render(request, 'query.html', {
                "videos": video,
                'search_term': search_term,
                'search_filter': search_filter
            })
        else:
            raise ValueError("Certifique que escreveste 'Ficha' ou 'Video'")

    else:
        return render(request, 'query.html')



