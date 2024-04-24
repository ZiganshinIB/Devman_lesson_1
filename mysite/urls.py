
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('journey.urls', namespace='journey')),
    path('tinymce/', include('tinymce.urls')),
]
