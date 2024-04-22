from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase

from . models import Place, ImagePlace
# Register your models here.


class ImagePlaceInline(SortableTabularInline):
    readonly_fields = ('get_preview',)
    model = ImagePlace
    def get_preview(self, obj):
        return format_html('<img src="{url}" width="200" />', url = obj.image.url, )
    fields = ('title', 'image', 'get_preview', 'position')
    ordering = ('position',)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'description_short', 'is_published')
    list_filter = ('is_published', 'created_at', 'updated_at')
    list_editable = ('is_published', 'description_short')
    search_fields = ('title', 'description')
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImagePlaceInline]


@admin.register(ImagePlace)
class ImagePlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return format_html('<img src="{url}" height="200"/> '.format(url = obj.image.url, ))

    list_display_links = ('title',)
    list_display = ('title', 'place', 'position')
    list_filter = ('place', 'created_at', 'updated_at')
    list_editable = ('position',)
    search_fields = ('title', 'place__title')
    ordering = ('position', 'title',)
