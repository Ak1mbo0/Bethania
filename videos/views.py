from django.shortcuts import render
from django.views.generic import ListView
from upload.models import Video

# Create your views here.

class Video_list_view(ListView):
    template_name = "video.html"
    model = Video
    queryset = Video.objects.filter(Status='p')
    context_object_name = 'videos'

