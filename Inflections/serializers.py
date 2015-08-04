from Inflections.models import Inflection
from rest_framework import serializers


class InflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflection
        fields = ('spelling', 'stem', 'pattern', 'attributes')
