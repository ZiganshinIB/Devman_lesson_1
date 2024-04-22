from django.db import models
from django.urls import reverse, resolve
from django.utils.text import slugify

# Create your models here.


class PlaceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Place(models.Model):
    objects = PlaceManager()
    market_label = models.CharField(max_length=100, db_index=True, verbose_name='Маркет')
    place_id = models.CharField(max_length=100, db_index=True, unique=True, verbose_name='ID места')
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    description_short = models.TextField(verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (['slug', 'title'])
        ordering = ['title']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('place', kwargs={'slug': self.slug})


class ImagePlace(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='media/', verbose_name='Изображение')
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, related_name='images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    position = models.PositiveIntegerField(verbose_name='Позиция', default=1)

    class Meta:
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображения мест'
        ordering = ['position']
        # unique_together = ('place', 'position')

    def get_absolute_url(self):
        return self.image.url

    def __str__(self):
        return self.title
