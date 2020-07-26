from django.shortcuts import render
from django.http import Http404
from .models import Music



# Create your views here.


def index(request):
    music = Music.objects.all()
    return render(request ,'index.html', {'music': music})

def search(request):
    search_term = ""
    search_term = request.GET['search']

    result = Music.objects.filter(name__icontains=search_term)
    if len(result) <= 0:
        result = Music.objects.filter(desc__icontains=search_term)
    elif len(result) >= 1:
        result = Music.objects.filter(name__icontains=search_term)
    elif len(result) >= 1:
        return Http404()
 
 
    return render(request, 'search.html', {"search": search_term, 'result': result})


def music(request, myid):
    music_return =  Music.objects.filter(id=myid)
    print(music_return)
    return render(request, 'music.html', {'music1': music_return[0]})
