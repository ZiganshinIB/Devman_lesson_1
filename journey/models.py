from django.db import models

from tinymce.models import HTMLField


class BaseTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PlaceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Place(BaseTimeModel):

    title = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    long_description = HTMLField(blank=True, verbose_name='Описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    is_published = models.BooleanField(default=True)

    objects = PlaceManager()

    class Meta:
        ordering = ['title']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class ImagePlace(BaseTimeModel):
    image = models.ImageField(verbose_name='Изображение')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    position = models.PositiveIntegerField(verbose_name='Позиция', default=0)

    class Meta:
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображения мест'
        ordering = ['position']

    def __str__(self):
        return self.image.name
