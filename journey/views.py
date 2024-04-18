from django.shortcuts import render
from  django.http import HttpResponse
from . models import Place

# Create your views here.
def index(request):
    places = Place.objects.all()
    context = {'places': places}
    return render(request, 'journey/index.html', context)