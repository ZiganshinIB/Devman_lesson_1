from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase

from . models import Place, ImagePlace


class ImagePlaceInline(SortableTabularInline):
    readonly_fields = ('get_preview',)
    model = ImagePlace

    def get_preview(self, obj):
        return format_html('<img src="{url}"  style="max-height: 200px; max-width: 200px;" />', url=obj.image.url, )
    fields = ('image', 'get_preview', 'position')
    ordering = ('position',)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'short_description', 'is_published')
    list_filter = ('is_published', 'created_at', 'updated_at')
    list_editable = ('is_published', 'short_description')
    search_fields = ('title', 'long_description')
    ordering = ('title',)
    inlines = [ImagePlaceInline]


@admin.register(ImagePlace)
class ImagePlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return format_html('<img src="{url}" style="'
                           'max-height: 200px;'
                           'max-width: 200px;"/> '.format(url=obj.image.url))

    raw_id_fields = ('place',)
    list_display = ('place', 'position')
    list_filter = ('created_at', 'updated_at')
    list_editable = ('position',)
    ordering = ('position',)
