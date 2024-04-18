from django.shortcuts import render, redirect
from  django.http import HttpResponse
from . models import Place, ImagePlace

# Create your views here.
def index(request):
    places = Place.objects.all()
    context = {'places': places}
    return render(request, 'journey/index.html', context)


def image_detail(request, image_id):
    image = ImagePlace.objects.get(id=image_id)
    context = {'image': image}
    return redirect(image.get_absolute_url())
