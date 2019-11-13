from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView
from .models import Video

# Create your views here.

def query(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['pdf']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'query.html', context)

class VideoListView(ListView):
    model = Video
    template_name = 'video_list.html'
    context_object_name = 'videos'