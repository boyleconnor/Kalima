from Dictionary.models import Word, Deriver
from rest_framework.serializers import ModelSerializer


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word


class DeriverSerializer(ModelSerializer):
    class Meta:
        model = Deriver