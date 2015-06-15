from ArabicTools.constants import POS_CHOICES, ABJAD
from ArabicTools.utils import pattern_to_form, apply, strip_diacritics
from django.db.models import Model, CharField, ForeignKey, TextField
from rest_framework.reverse import reverse_lazy


class Pattern(Model):
    origin_pos = CharField(max_length=16, choices=POS_CHOICES)
    result_pos = CharField(max_length=16, choices=POS_CHOICES)
    origin_form = CharField(default=('([%s])' % ABJAD) * 3, max_length=255)
    result_form = CharField(max_length=255)
    origin_pattern = ForeignKey('self', blank=True, null=True, related_name='result_patterns')
    example_stem = ForeignKey('Word', blank=True, null=True, related_name='example_in')
    name = CharField(max_length=63, blank=True)

    def get_origin_form_display(self):
        return pattern_to_form(self.origin_form)

    def get_result_form(self):
        if self.example_stem:
            return self.apply(self.example_stem)
        if self.origin_pattern:
            return self.apply(self.origin_pattern.get_result_form())
        else:
            return None

    def apply_spelling(self, word):
        return apply(self.origin_form, word.spelling, self.result_form)

    def apply(self, stem, save=False, **kwargs):
        result = Word(spelling=self.apply_spelling(stem), stem=stem, pattern=self, pos=self.result_pos, **kwargs)
        if save:
            result.save()
        return result

    def get_absolute_url(self):
        return reverse_lazy('dictionary:pattern.detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s (%s)' % (self.name, self.get_result_form()) if self.get_result_form() else self.name


class Word(Model):
    pos = CharField(max_length=20, choices=POS_CHOICES)
    spelling = CharField(max_length=255)
    definition = TextField()
    examples = TextField(blank=True)
    stem = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    pattern = ForeignKey('Dictionary.Pattern', blank=True, null=True, related_name='words')

    def get_root(self):
        stem = self.stem
        if stem is None:
            return None
        elif stem.pos == 'root':
            return stem
        else:
            return stem.get_root()

    def get_without_diacritics(self):
        return strip_diacritics(self.spelling)

    def get_absolute_url(self):
        return reverse_lazy('dictionary:word.detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.spelling