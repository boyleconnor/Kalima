from ArabicTools.utils import transcribe, strip_diacritics, apply, template_to_form
from django.core.urlresolvers import reverse_lazy
from django.db.models import Model, ForeignKey, CharField, TextField
from ArabicTools.constants import POS_CHOICES, ARABIZI, SHADDA


class Word(Model):
    pos = CharField(choices=POS_CHOICES, max_length=15)
    spelling = CharField(max_length=255)
    definition = TextField()
    examples = TextField(blank=True)
    stem = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    pattern = ForeignKey('Deriver', blank=True, null=True, related_name='words')

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

    def get_key_spelling(self):
        return strip_diacritics(self.spelling, (SHADDA,))

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


class Deriver(Model):
    origin_pos = CharField(choices=POS_CHOICES, max_length=15)
    result_pos = CharField(choices=POS_CHOICES, max_length=15)
    origin_form = CharField(default='xxx', max_length=255)
    result_form = CharField(max_length=255)
    name = CharField(max_length=63, blank=True)

    def get_origin_form_display(self):
        return template_to_form(self.origin_form)

    def get_result_form_display(self):
        return template_to_form(self.result_form)

    def apply_spelling(self, word):
        if type(word) is not Word:
            raise TypeError('Type of ''word'' must be ''str''')
        return apply(word.get_root().spelling)

    def apply(self, stem):
        return Word(spelling=self.apply_spelling(stem), pos=self.result_pos, stem=stem, pattern=self)

    def apply_and_save(self, stem):
        result = self.apply(stem)
        result.save()
        return result

    def get_update_url(self):
        pass

    def get_detail_url(self):
        return reverse_lazy('dictionary:deriver.detail', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return self.get_detail_url()

    def __str__(self):
        return self.name