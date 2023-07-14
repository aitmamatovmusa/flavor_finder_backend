from django.urls import path

from .views import PlaceListView

urlpatterns = [
    path("places/", PlaceListView.as_view()),
]
