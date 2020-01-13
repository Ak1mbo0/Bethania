from django.shortcuts import render
from upload.models import Video, Ficha
# Create your views here.


def visualizar_view(request):
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

    else:
        return render(request, 'video.html')
