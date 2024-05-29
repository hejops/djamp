from django.shortcuts import render
from django.views import generic

from artists.models import Artist


class IndexView(generic.ListView):
    template_name = "artists/index.html"  # default: <app name>/<model name>_list.html

    context_object_name = "artist_list"

    def get_queryset(self):  # -> _SupportsPagination[_M]:
        # return Artist.objects.all()  # .order_by("pk")
        return Artist.objects.filter().order_by("name")


class DetailView(generic.DetailView):
    model = Artist
