from rest_framework import serializers

from api.models import Event, Person


class EventSerializer(serializers.ModelSerializer):

	class Meta:
		model = Event
		fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = "__all__"
