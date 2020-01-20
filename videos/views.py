from django.shortcuts import render
from upload.models import Video, Ficha, Aula
# Create your views here.


def visualizar_view(request):
    if 'view_filter' in request.GET:
        view_filter = request.GET['view_filter']
        if view_filter == 'visualizar_fichas':
            print(view_filter)
            ficha = Ficha.objects.all()
            return render(request, 'video.html', {
                "fichas": ficha,
                "view_filter": view_filter,
            })
        elif view_filter == 'visualizar_videos':
            print(view_filter)
            video = Video.objects.all()
            return render(request, 'video.html', {
                "videos": video,
                "view_filter": view_filter,
            })
        elif view_filter == 'visualizar_aulas':
            print(view_filter)
            aula = Aula.objects.all()
            return render(request, 'video.html', {
                "aulas": aula,
                "view_filter": view_filter,
            })

        else:
            return render(request, 'video.html')
    else:
        return render(request, 'video.html')
