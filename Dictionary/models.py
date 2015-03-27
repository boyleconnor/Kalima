from ArabicTools.utils import transcribe, strip_diacritics, apply, pattern_to_form
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse_lazy
from django.db.models import Model, ForeignKey, CharField, TextField
from ArabicTools.constants import POS_CHOICES, ARABIZI, SHADDA, ABJAD, DEFAULT_ROOT_SPELLING, NUMBER_CHOICES, \
    GENDER_CHOICES, STATE_CHOICES, PERSON_CHOICES, TENSE_CHOICES, CASE_CHOICES
from django.utils.translation import ugettext_lazy as trans


class Word(Model):
    class Meta:
        abstract = True
    spelling = CharField(max_length=255)
    definition = TextField(trans('Definition'))
    examples = TextField(trans('Examples'), blank=True)
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
    origin_form = CharField(default=('([%s])' % ABJAD) * 3, max_length=255)
    result_form = CharField(max_length=255)
    origin_pattern = ForeignKey('self', blank=True, null=True, related_name='result_patterns')
    name = CharField(max_length=63, blank=True)

    def get_origin_form_display(self):
        return pattern_to_form(self.origin_form)

    def get_result_form(self):
        if self.origin_pos == 'root':
            return self.apply(Word(spelling=DEFAULT_ROOT_SPELLING, pos='root'))
        return self.apply(self.origin_pattern.get_result_form())

    def get_result_form_display(self):
        return self.get_result_form().spelling

    def apply_spelling(self, word):
        if type(word) is not Word:
            raise TypeError('Type of argument ''word'' must be ''Word''')
        return apply(self.origin_form, word.spelling, self.result_form)

    def apply(self, stem, save=False):
        result = Word(spelling=self.apply_spelling(stem), pos=self.result_pos, stem=stem, pattern=self)
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
        return self.name


class Inflection(Model):
    stem = ForeignKey(Word)
    pattern = ForeignKey('Inflecter')
    spelling = CharField(max_length=250)
    case = CharField(max_length=20, choices=CASE_CHOICES, blank=True)
    number = CharField(max_length=20, choices=NUMBER_CHOICES, blank=True)
    state = CharField(max_length=20, choices=STATE_CHOICES, blank=True)
    gender = CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    person = CharField(max_length=20, choices=PERSON_CHOICES, blank=True)
    tense = CharField(max_length=20, choices=TENSE_CHOICES, blank=True)

    def __str__(self):
        return self.spelling


class Inflecter(Model):
    origin_pattern = ForeignKey(Deriver)
    origin_form = CharField(max_length=255)
    result_form = CharField(max_length=255)
    case = CharField(max_length=20, choices=CASE_CHOICES, blank=True)
    number = CharField(max_length=20, choices=NUMBER_CHOICES, blank=True)
    state = CharField(max_length=20, choices=STATE_CHOICES, blank=True)
    gender = CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    person = CharField(max_length=20, choices=PERSON_CHOICES, blank=True)
    tense = CharField(max_length=20, choices=TENSE_CHOICES, blank=True)

    def get_origin_form_display(self):
        return pattern_to_form(self.origin_form)

    def get_result_form(self):
        return self.apply(self.origin_pattern.get_result_form())

    def get_result_form_display(self):
        return self.get_result_form().spelling

    def apply_spelling(self, word):
        if type(word) is not Word:
            raise TypeError('Type of argument ''word'' must be ''Word''')
        return apply(self.origin_form, word.spelling, self.result_form)

    def apply(self, stem, save=False):
        result = Inflection(spelling=self.apply_spelling(stem), stem=stem, pattern=self, **self.get_attributes())
        if save:
            result.save()
        return result

    def get_attributes(self):
        attributes = dict()
        for attribute in ['case', 'state', 'number', 'gender', 'person', 'tense']:
            attributes[attribute] = getattr(self, attribute)
        return attributes

    def get_attributes_display(self):
        attributes = str()
        if self.case:
            attributes += '%s ' % self.case
        if self.state:
            attributes += '%s ' % self.state
        if self.number:
            attributes += '%s ' % self.number
        if self.gender:
            attributes += '%s ' % self.gender
        if self.person:
            attributes += '%s person' % self.tense
        if self.tense:
            attributes += '%s '
        attributes += 'inflection'
        return attributes

    def __str__(self):
        return '%s: %s' % (self.get_attributes(), self.get_result_form_display())
