from django.urls import path

from . import views

app_name = "artists"

urlpatterns = [
    # https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path
    path(
        route="",
        view=views.IndexView.as_view(),
        name="index",
    ),
    path(
        # generally, str won't work
        # route="<str:name>/",
        route="<int:pk>/",
        view=views.DetailView.as_view(),
        name="detail",
    ),
]
