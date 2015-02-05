from Dictionary.models import Word, Deriver
from django.forms import ModelForm
from haystack.forms import SearchForm


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = '__all__'


class DeriverForm(ModelForm):
    class Meta:
        model = Deriver
        fields = '__all__'


class WordSearchForm(SearchForm):
    pass