from Inflections.models import Inflection, Stem
from rest_framework import serializers


class InflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflection
        fields = ('spelling', 'stem', 'pattern', 'attributes')


class StemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stem
        fields = ('spelling', 'parent', 'parent', 'exemplar', 'attributes')
