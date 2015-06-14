from Dictionary.models import Word, Pattern
from rest_framework.serializers import ModelSerializer


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = ('pos', 'spelling', 'definition', 'examples', 'stem', 'pattern')


class PatternSerializer(ModelSerializer):
    class Meta:
        model = Pattern
        fields = ('origin_pos', 'result_pos', 'origin_form', 'result_form', 'origin_pattern', 'example_stem', 'name')