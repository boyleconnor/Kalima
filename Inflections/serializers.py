from Inflections.models import Inflection, Stem, Stemmer, Paradigm, Inflecter
from rest_framework import serializers


class InflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflection
        fields = ('id', 'spelling', 'stem', 'pattern', 'attributes')


class StemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stem
        fields = ('id', 'spelling', 'parent', 'parent', 'exemplar', 'attributes')


class StemmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stemmer
        fields = ('id', 'origin_form', 'get_origin_form', 'result_form', 'get_result_form', 'origin_pattern')


class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'name',)


class InflecterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflecter
        fields = ('id', 'paradigm', 'attributes', 'prefix', 'suffix')
