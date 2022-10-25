from django.urls import path

from .views import ReportList, ReportDetail, ReportCreate

urlpatterns = [
    path("<int:pk>/", ReportDetail.as_view(), name="report-details"),
    path("create/", ReportCreate.as_view(), name="report-create"),
    path("", ReportList.as_view(), name="report-list"),
]
