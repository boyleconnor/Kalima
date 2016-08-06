from Dictionary.models import Word, Pattern
from django.forms import ModelForm, Form, ModelChoiceField, CharField
from django.forms.widgets import Textarea, HiddenInput
from haystack.forms import SearchForm


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = '__all__'


class PatternForm(ModelForm):
    class Meta:
        model = Pattern
        fields = '__all__'


class WordSearchForm(SearchForm):
    pass


class PatternApplyForm(Form):
    stem = ModelChoiceField(queryset=Word.objects.all())

    def apply(self, pattern, save=True):
        return pattern.apply(self.cleaned_data['stem'], save)
