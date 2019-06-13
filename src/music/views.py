from django.shortcuts import render, get_object_or_404
from .models import Album


# Create your views here.


def index(request):

	all_albums = Album.objects.all()

	template = 'music/index.html'

	context = {'all_albums': all_albums}

	return render(request, template, context)


def detail(request, album_id):

	album = get_object_or_404(Album, id=album_id)
	
	template = 'music/detail.html'
	context = {'album':album}
	return render(request, template, context)
