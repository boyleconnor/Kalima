from ArabicTools.utils import form_to_template
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

    def save(self, commit=True):
        instance = super(DeriverForm, self).save(commit=False)
        instance.origin_form = form_to_template(instance.origin_form)
        instance.result_form = form_to_template(instance.result_form)
        if commit:
            instance.save()
        return instance


class WordSearchForm(SearchForm):
    pass