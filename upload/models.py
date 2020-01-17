from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField

# Create your models here.
STATUS_CHOICES = [
    ('p', 'Published'),
    ('h', 'Hidden'),
]

class Ficha(models.Model):
    Titulo = models.CharField(max_length=40)
    Tema = models.CharField(max_length=40, null=True)
    Documento = models.FileField(upload_to='pdf/')
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='h')
    Tipo = models.CharField(max_length=40, default='Ficha')
    Periodo = models.CharField(max_length=1, default=1)

    def __str__(self):
        return self.Titulo


class Video(models.Model):
    Video = EmbedVideoField(verbose_name="Video")
    Titulo = models.CharField(max_length=40)
    Tema = models.CharField(max_length=40)
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='h')
    Tipo = models.CharField(max_length=40, default='Video')
    Periodo = models.CharField(max_length=1, default=1)

    def unicode(self):
        return self.Titulo

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

