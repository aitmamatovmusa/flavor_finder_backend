from django.urls import path

from .views import PlaceList, PlaceDetail, CommentList

urlpatterns = [
    path("places/", PlaceList.as_view()),
    path("places/<int:pk>/", PlaceDetail.as_view()),
    path("comments/", CommentList.as_view()),
]
