from django.urls import path

from .views import EventsList, EventsDetail, EventCreate

urlpatterns = [
    path("<int:pk>/", EventsDetail.as_view(), name="events-details"),
    path("create/", EventCreate.as_view(), name="events-create"),
    path("", EventsList.as_view(), name="events-list"),
]
