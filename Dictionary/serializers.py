from Dictionary.models import Word, Pattern
from django.core.exceptions import ValidationError
from rest_framework import serializers


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'pos', 'spelling', 'definition', 'examples', 'parent', 'pattern')


class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = ('id', 'origin_pos', 'result_pos', 'origin_form', 'result_form', 'origin_pattern', 'example_stem', 'name', 'get_origin_form_display', 'get_result_form_display')


class ApplySerializer(serializers.Serializer):
    pattern = serializers.PrimaryKeyRelatedField(queryset=Pattern.objects.all())
    parent = serializers.PrimaryKeyRelatedField(queryset=Word.objects.all())

    def validate(self, data):
        if Word.objects.filter(pattern=data['pattern'], stem=data['parent']):
            raise ValidationError('pattern must not already be applied to this stem')
        if data['pattern'].origin_pos != data['parent'].pos:
            raise ValidationError('pattern\'s origin part of speech must match parent\'s part of speech')
        return data

    def create(self, validated_data):
        pattern = validated_data['pattern']
        parent = validated_data['parent']
        return pattern.apply(parent, save=True)

    def to_representation(self, instance):
        return WordSerializer().to_representation(self.instance)
