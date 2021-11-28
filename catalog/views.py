from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Events
from .serializers import EventsSerializer

# # Create your views here.

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by('gender')
    serializer_class = EventsSerializer