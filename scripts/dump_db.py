"""Scan music directory and populate db with artists and albums"""

import os

from artists.models import Album
from artists.models import Artist

LIBRARY_ROOT = os.environ["MU"]

# don't sort, because the os always returns dirs in a deterministic order
for a in os.scandir(LIBRARY_ROOT):
    # with unique=True, attempting to duplicate an artist raises IntegrityError
    # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#get-or-create
    artist, new = Artist.objects.get_or_create(name=a.name)
    if new:
        artist.save()

    # https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_one/
    # ForeignKey = parent.child_set.create(...)
    for alb in os.scandir(a.path):
        if not alb.name.endswith(")"):
            continue
        try:
            alb, year = alb.name.rsplit(maxsplit=1)
            year = int(year.strip("()"))
        except ValueError:
            print("skipped", a.name, alb)
            continue
        album, new = artist.album_set.get_or_create(
            name=alb,
            year=year,
        )
        # if new:
        #     print("created", a.name, alb)

    # # ManyToManyField = child.parent.add(parent)
    # # ManyToManyField is incompatible with constraints!
    # for alb in os.scandir(a.path):
    #     if not alb.name.endswith(")"):
    #         continue
    #     album = Album(name=alb)
    #     album.save()
    #     album.artist.add(artist)

print(
    len(Artist.objects.all()),
    "artists",
    len(Album.objects.all()),
    "albums",
)
