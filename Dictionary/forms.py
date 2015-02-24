from Dictionary.models import Word, Deriver
from django.forms import ModelForm, Form, ModelChoiceField, CharField
from django.forms.widgets import Textarea, HiddenInput
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


class DeriverApplyForm(Form):
    stem = ModelChoiceField(queryset=Word.objects.all())
    deriver = ModelChoiceField(queryset=Deriver.objects.all(), widget=HiddenInput())

    def apply(self, deriver, save=True):
        return deriver.apply(self.cleaned_data['stem'], save)