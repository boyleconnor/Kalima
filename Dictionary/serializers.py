from Dictionary.models import Word, Deriver
from rest_framework.serializers import ModelSerializer


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = ('pos', 'spelling', 'definition', 'examples', 'stem', 'pattern')


class DeriverSerializer(ModelSerializer):
    class Meta:
        model = Deriver
        fields = ('origin_pos', 'result_pos', 'origin_form', 'result_form', 'origin_pattern', 'example_stem', 'name')