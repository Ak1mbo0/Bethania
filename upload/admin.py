from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

####

class FichaAdmin(admin.ModelAdmin):
    list_display = ['Titulo', 'Tema', 'Documento', 'Status']
    ordering = ['Tema']
    actions = ['make_published', 'make_hidden']

    def make_published(modeladmin, request, queryset):
        queryset.update(Status='p')

    make_published.short_description = "Publicar itens selecionados"

    def make_hidden(modeladmin, request, queryset):
        queryset.update(Status='h')

    make_hidden.short_description = "Esconder itens selecionados"


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('Video', 'Titulo', 'Tema', 'Status')
    ordering = ['Tema']
    actions = ['make_published', 'make_hidden']

    def make_published(modeladmin, request, queryset):
        queryset.update(Status='p')

    make_published.short_description = "Publicar itens selecionados"
    def make_hidden(modeladmin, request, queryset):
        queryset.update(Status='h')

    make_hidden.short_description = "Esconder itens selecionados"


# Register your models here.
admin.site.register(Ficha)
admin.site.register(Video, MyModelAdmin)



