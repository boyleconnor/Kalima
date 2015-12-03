from django_filters import FilterSet, ModelChoiceFilter
from Inflections.models import Inflection, Stem
from Dictionary.models import Word


class InflectionFilter(FilterSet):
    word = ModelChoiceFilter(queryset=Word.objects.all(), name='stem__parent')
    class Meta:
        model = Inflection
        fields = ['word']


class StemFilter(FilterSet):
    word = ModelChoiceFilter(queryset=Word.objects.all(), name='parent')
    class Meta:
        model = Stem
        fields = ['word', 'parent']
