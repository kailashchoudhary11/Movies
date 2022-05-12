from django.urls import path
from .views import MovieDetails, saved
app_name = "moviedetails"

urlpatterns = [
    path("", MovieDetails.as_view(), name="details"),
    path("saved", saved, name="saved"),
]
