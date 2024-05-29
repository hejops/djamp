from django.db import models

# ./manage.py migrate
# ./manage.py makemigrations
# ./manage.py migrate


# https://stackoverflow.com/q/66142733

# artists must be unique
# an artist has one or more albums
#
# albums must not be unique (e.g. 'Demo')
# an album is 'owned' by one or more artists


class Artist(models.Model):
    name = models.TextField(unique=True)

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    name = models.TextField()

    artist = models.ForeignKey(
        to=Artist,
        on_delete=models.CASCADE,
        # verbose_name="Journal",
    )

    # artist = models.ManyToManyField(to=Artist)

    year = models.IntegerField(
        # TODO: int bounds, or year-only date
        # min_value="1920",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["artist", "name", "year"],
                name="artist_album_year",
            )
        ]

    def __str__(self) -> str:
        return self.name

    # def __repr__(self) -> str:
    #     return f"Album: {self.name}"  # \nYear: {self.year}"
    #
    # def get_artist(self):  # -> Artist:
    #     return self.artist.values_list("name")
    #
    # def as_dict(self) -> dict:
    #     return {
    #         "Album": self.name,
    #         "Artist": self.artist,
    #         "Year": self.year,
    #     }
