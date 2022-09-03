from django.urls import path

from .views import SpeakersList, SpeakersDetail, SpeakersCreate

urlpatterns = [
    path("<int:pk>/", SpeakersDetail.as_view(), name="speaker-details"),
    path("create/", SpeakersCreate.as_view(), name="speaker-create"),
    path("", SpeakersList.as_view(), name="speakers-list"),
]
