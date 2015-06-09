from ArabicTools.constants import DEFAULT_ROOT_SPELLING, POS_CHOICES, ABJAD, GENDER_CHOICES
from ArabicTools.utils import pattern_to_form, apply
from Dictionary.models.Words import Word
from django.db.models import Model, CharField, ForeignKey
from rest_framework.reverse import reverse_lazy


class Deriver(Model):
    class Meta:
        app_label = 'Dictionary'
    origin_pos = CharField(max_length=16, choices=POS_CHOICES)
    result_pos = CharField(max_length=16, choices=POS_CHOICES)
    origin_form = CharField(default=('([%s])' % ABJAD) * 3, max_length=255)
    result_form = CharField(max_length=255)
    origin_pattern = ForeignKey('self', blank=True, null=True, related_name='result_patterns')
    example_stem = CharField(max_length=4, blank=True)
    name = CharField(max_length=63, blank=True)

    def get_origin_form_display(self):
        return pattern_to_form(self.origin_form)

    def get_result_form(self):
        if self.example_stem:
            return self.apply(Word(spelling=self.example_stem, pos=self.origin_pos))
        return self.apply(self.origin_pattern.get_result_form())

    def get_result_form_display(self):
        return self.get_result_form().spelling

    def apply_spelling(self, word):
        return apply(self.origin_form, word.spelling, self.result_form)

    def apply(self, stem, save=False, **kwargs):
        result = Word(spelling=self.apply_spelling(stem), stem=stem, pattern=self, pos=self.result_pos, **kwargs)
        if save:
            result.save()
        return result

    def get_update_url(self):
        return reverse_lazy('dictionary:deriver.update', kwargs={'pk': self.pk})

    def get_apply_url(self):
        return reverse_lazy('dictionary:deriver.apply', kwargs={'pk': self.pk})

    def get_detail_url(self):
        return reverse_lazy('dictionary:deriver.detail', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return self.get_detail_url()

    def __str__(self):
        return '%s (%s)' % (self.name, self.get_result_form_display())