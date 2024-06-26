from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'journey'

urlpatterns = [
    path('', views.index, name='index'),
    path('places/<int:pk>/', views.place, name='place'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
