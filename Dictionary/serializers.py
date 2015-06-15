from Dictionary.models import Word, Pattern
from django.core.exceptions import ValidationError
from rest_framework import serializers


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('pos', 'spelling', 'definition', 'examples', 'stem', 'pattern')


class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = ('origin_pos', 'result_pos', 'origin_form', 'result_form', 'origin_pattern', 'example_stem', 'name')


class ApplySerializer(serializers.Serializer):
    pattern = serializers.PrimaryKeyRelatedField(queryset=Pattern.objects.all())
    parent = serializers.PrimaryKeyRelatedField(queryset=Word.objects.all())

    def validate(self, data):
        if Word.objects.filter(pattern=data['pattern'], stem=data['parent']):
            raise ValidationError('pattern must not already be applied to this stem')
        return data

    def create(self, validated_data):
        pattern = validated_data['pattern']
        parent = validated_data['parent']
        spelling = pattern.apply_spelling(parent)
        return Word.objects.create(pattern=pattern, stem=parent, spelling=spelling)

    def to_representation(self, instance):
        return WordSerializer().to_representation(self.instance)