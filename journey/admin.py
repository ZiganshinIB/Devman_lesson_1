from django.contrib import admin

from . models import Place, ImagePlace
# Register your models here.


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short', 'is_published')
    list_filter = ('is_published', 'created_at', 'updated_at')
    list_editable = ('is_published', 'description_short')
    search_fields = ('title', 'description')
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ImagePlace)
class ImagePlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'place')
    list_filter = ('place', 'created_at', 'updated_at')
    search_fields = ('title', 'place__title')
    ordering = ('place__title', 'title',)
