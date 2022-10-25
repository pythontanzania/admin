from rest_framework import generics, permissions

from django.shortcuts import render

from .models import Report
from .serializers import ReportSerializer

class ReportList(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser, )
    serializer_class = ReportSerializer

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

