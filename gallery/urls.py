from django.urls import path

from .views import GalleryList, GalleryDetail, GalleryCreate

urlpatterns = [
    path("<int:pk>/", GalleryDetail.as_view(), name="gallery-details"),
    path("create/", GalleryCreate.as_view(), name="gallery-create"),
    path("", GalleryList.as_view(), name="gallery-list"),
]
