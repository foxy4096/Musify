from django.shortcuts import render, get_object_or_404
from .models import Music
from django.db.models import Q


# Create your views here.


def index(request):
    music = Music.objects.all()
    return render(request, "index.html", {"music": music})


def search(request):
    search_term = request.GET.get("search", "")
    musics = Music.objects.filter(
        Q(name__icontains=search_term)
        | Q(desc__icontains=search_term)
        | Q(category__icontains=search_term)
    )
    return render(request, "search.html", {"search": search_term, "result": musics})


def music_details(request, myid):
    music_return = get_object_or_404(Music, pk=myid)
    print(music_return)
    return render(request, "music.html", {"music1": music_return})
