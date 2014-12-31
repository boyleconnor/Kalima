from ArabicTools.utils import transcribe, strip_diacritics
from django.core.urlresolvers import reverse_lazy
from django.db.models import Model, ForeignKey, CharField, TextField
import re
from ArabicTools.constants import POS_CHOICES, ABJAD, ARABIZI, SHADDA, DEFAULT_ROOT_ID


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
    expectation = CharField(default=(('([%s])' % ABJAD) * 3), max_length=255)
    template = CharField(max_length=255)
    name = CharField(max_length=63, blank=True)

    def get_expectation_display(self):
        return self.expectation

    def get_template_display(self):
        default_root = Word.objects.get(id=DEFAULT_ROOT_ID)
        return self.apply_spelling(default_root)

    def apply_spelling(self, word_in):
        if type(word_in) is not Word:
            raise TypeError('Type of ''word_in'' must be ''dictionary.Word''')
        return re.match(self.expectation, word_in.spelling).expand(self.template)

    def apply(self, stem):
        return Word(spelling=self.apply_spelling(stem), pos=self.result_pos, stem=stem, pattern=self)

    def apply_and_save(self, stem):
        result = self.apply(stem)
        result.save()
        return result

    def get_update_url(self):
        pass

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.name