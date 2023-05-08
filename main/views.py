from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PatientSerializer
from . import models

class PatientList(generics.ListCreateAPIView):
    queryset = models.Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Patient.objects.all()
    serializer_class = PatientSerializer