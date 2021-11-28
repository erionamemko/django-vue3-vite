from rest_framework import serializers
from .models import Events


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ('gender', 'age', 'country', 'segments')

