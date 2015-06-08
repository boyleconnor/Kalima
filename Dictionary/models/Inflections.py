from ArabicTools.constants import CASE_CHOICES, NUMBER_CHOICES, STATE_CHOICES, GENDER_CHOICES, PERSON_CHOICES, \
    TENSE_CHOICES, VOICE_CHOICES
from django.db.models import ForeignKey, Model, CharField


class Inflection(Model):
    class Meta:
        app_label = 'Dictionary'
    stem = ForeignKey('Dictionary.Word')
    pattern = ForeignKey('Dictionary.Inflecter', blank=True, null=True)
    spelling = CharField(max_length=250)

    case = CharField(max_length=20, choices=CASE_CHOICES, blank=True)
    state = CharField(max_length=20, choices=STATE_CHOICES, blank=True)
    number = CharField(max_length=20, choices=NUMBER_CHOICES, blank=True)
    gender = CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    person = CharField(max_length=20, choices=PERSON_CHOICES, blank=True)
    tense = CharField(max_length=20, choices=TENSE_CHOICES, blank=True)
    voice = CharField(max_length=20, choices=VOICE_CHOICES, blank=True)

    def __str__(self):
        return self.spelling

