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
    pattern = ForeignKey('Deriver', blank=True, null=True, related_name='words')

    def get_root(self):
        stem = self.stem
        if stem is None:
            return None
        elif type(stem) == Root:
            return stem
        else:
            return stem.get_root()

    def get_arabizi(self):
        return transcribe(self.spelling, ARABIZI)

    def get_without_diacritics(self):
        return strip_diacritics(self.spelling)

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


class Root(Word):
    length = SmallIntegerField(choices=ROOT_LENGTH_CHOICES)


class Noun(Word):
    gender = CharField(max_length=20, choices=GENDER_CHOICES)
    human = BooleanField(default=False)


class Adjective(Word):
    noun = ManyToManyField(Noun)


class Adverb(Word):
    pass


class Verb(Word):
    noun = ManyToManyField(Noun)