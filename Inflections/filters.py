from django_filters import FilterSet, ModelChoiceFilter
from Inflections.models import Inflection
from Dictionary.models import Word


class InflectionFilter(FilterSet):
    word = ModelChoiceFilter(queryset=Word.objects.all(), name='stem__parent')
    class Meta:
        model = Inflection
        fields = ['word']
