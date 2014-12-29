from Dictionary.models import Word
from django.forms import ModelForm
from haystack.forms import SearchForm


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = '__all__'


class WordSearchForm(SearchForm):
    pass