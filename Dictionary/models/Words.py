from ArabicTools.constants import ARABIZI, SHADDA, POS_CHOICES, GENDER_CHOICES, ROOT_LENGTH_CHOICES
from ArabicTools.utils import strip_diacritics, transcribe
from django.core.urlresolvers import reverse_lazy
from django.db.models import SmallIntegerField, CharField, BooleanField, ForeignKey, TextField, Model, ManyToManyField
from django.utils.translation import ugettext_lazy as trans


class Word(Model):
    class Meta:
        app_label = 'Dictionary'
    pos = CharField(max_length=20, choices=POS_CHOICES)
    spelling = CharField(max_length=255)
    definition = TextField(trans('Definition'))
    examples = TextField(trans('Examples'), blank=True)
    stem = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    pattern = ForeignKey('Dictionary.Deriver', blank=True, null=True, related_name='words')

    def get_root(self):
        stem = self.stem
        if stem is None:
            return None
        elif stem.pos == 'root':
            return stem
        else:
            return stem.get_root()

    def get_arabizi(self):
        return transcribe(self.spelling, ARABIZI)

    def get_without_diacritics(self):
        return strip_diacritics(self.spelling)

    def get_spelling_display(self):
        if self.pos == 'root':
            return ' '.join(self.spelling)
        else:
            return self.spelling

    def get_update_url(self):
        return reverse_lazy('dictionary:word.update', kwargs={'pk': self.pk})

    def get_detail_url(self):
        return reverse_lazy('dictionary:word.detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('dictionary:word.delete', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return self.get_detail_url()

    def __str__(self):
        return self.spelling