from rest_framework import viewsets

from api.models import Event, Person
from api.serializers import EventSerializer, PersonSerializer


class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer


class PersonViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer
