from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

####

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('Video', 'Titulo', 'Tema')


# Register your models here.
admin.site.register(Ficha)
admin.site.register(Video, MyModelAdmin)


