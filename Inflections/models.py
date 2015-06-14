from ArabicTools.constants import CASE_CHOICES, GENDER_CHOICES, STATE_CHOICES, NUMBER_CHOICES, PERSON_CHOICES, \
    TENSE_CHOICES, VOICE_CHOICES
from ArabicTools.utils import pattern_to_form, apply
from Dictionary.models.Patterns import Pattern
from django.db.models import Model, ForeignKey, CharField, TextField


class Inflection(Model):
    stem = ForeignKey('Dictionary.Word')
    pattern = ForeignKey('Inflections.Inflecter', blank=True, null=True)
    spelling = CharField(max_length=250)
    attributes = TextField()

    case = CharField(max_length=20, choices=CASE_CHOICES, blank=True)
    state = CharField(max_length=20, choices=STATE_CHOICES, blank=True)
    number = CharField(max_length=20, choices=NUMBER_CHOICES, blank=True)
    gender = CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    person = CharField(max_length=20, choices=PERSON_CHOICES, blank=True)
    tense = CharField(max_length=20, choices=TENSE_CHOICES, blank=True)
    voice = CharField(max_length=20, choices=VOICE_CHOICES, blank=True)

    def __str__(self):
        return self.spelling


class Inflecter(Model):
    origin_pattern = ForeignKey(Pattern)
    origin_form = CharField(max_length=255)
    result_form = CharField(max_length=255)

    case = CharField(max_length=20, choices=CASE_CHOICES, blank=True)
    state = CharField(max_length=20, choices=STATE_CHOICES, blank=True)
    number = CharField(max_length=20, choices=NUMBER_CHOICES, blank=True)
    gender = CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    person = CharField(max_length=20, choices=PERSON_CHOICES, blank=True)
    tense = CharField(max_length=20, choices=TENSE_CHOICES, blank=True)
    voice = CharField(max_length=20, choices=VOICE_CHOICES, blank=True)

    def get_origin_form_display(self):
        return pattern_to_form(self.origin_form)

    def get_result_form(self):
        return self.apply(self.origin_pattern.get_result_form())

    def get_result_form_display(self):
        return self.get_result_form().spelling

    def apply_spelling(self, word):
        return apply(self.origin_form, word.spelling, self.result_form)

    def apply(self, stem, save=False, **kwargs):
        result = Inflection(spelling=self.apply_spelling(stem), stem=stem, pattern=self, **kwargs)
        for attribute in ('case', 'state', 'number', 'gender', 'person', 'tense', 'voice'):
            setattr(result, attribute, getattr(self, attribute))
        if save:
            result.save()
        return result

    def __str__(self):
        return self.get_result_form_display()