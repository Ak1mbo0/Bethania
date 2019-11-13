from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField

# Create your models here.


class Ficha(models.Model):
    Titulo = models.CharField(max_length=40)
    Tema = models.CharField(max_length=40, null=True)
    Documento = models.FileField(upload_to='pdf/')

    def __str__(self):
        return self.Titulo


class Video(models.Model):
    Video = EmbedVideoField(verbose_name="Video")
    Titulo = models.CharField(max_length=40)
    Tema = models.CharField(max_length=40)

    def unicode(self):
        return self.Titulo

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

