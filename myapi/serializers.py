from rest_framework import serializers
from crud.models import *


class TracksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tracks
        fields = ['tr_id', 'name']


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

