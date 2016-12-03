import re
from ArabicTools.constants import POS_CHOICES
from ArabicTools.mixins import Spellable
from ArabicTools.models import Pattern
from django.db.models import Model, CharField, ForeignKey, OneToOneField, TextField
from rest_framework.reverse import reverse_lazy


class Word(Spellable):
    pos = CharField(max_length=20, choices=POS_CHOICES)
    definition = TextField()
    examples = TextField(blank=True)
    parent = ForeignKey('Word', blank=True, null=True, related_name='derivatives')
    deriver = ForeignKey('Dictionary.Deriver', blank=True, null=True, related_name='words')

    def get_root(self):
        stem = self.stem
        if stem is None:
            return None
        elif stem.pos == 'root':
            return stem
        else:
            return stem.get_root()

    def get_absolute_url(self):
        return reverse_lazy('main:word', kwargs={'pk': self.pk})

    def get_inflections(self):
        '''Returns each inflection associated with each stem associated with this word
        ''' 
        inflections  = []
        for stem in self.stem_set.all():
            for inflection in stem.inflection_set.all():
                inflections.append(inflection)
        return inflections 


class Deriver(Model):
    origin_deriver = ForeignKey('self', blank=True, null=True, related_name='result_derivers')
    origin_pos = CharField(max_length=16, choices=POS_CHOICES)
    result_pos = CharField(max_length=16, choices=POS_CHOICES)
    paradigm = ForeignKey('Inflections.Paradigm', blank=True, null=True)
    pattern = OneToOneField('ArabicTools.Pattern')
    name = CharField(max_length=63, blank=True)

    def apply(self, origin, *args, **kwargs):
        return Word.objects.create(
            spelling=self.pattern.generate_spelling(origin_spelling=origin.spelling),
            pos=self.result_pos,
            deriver=self,
            parent=origin
        )

    def get_absolute_url(self):
        return reverse_lazy('dictionary:pattern.detail', kwargs={'pk': self.pk})

    def get_potential_words(self):
        '''Returns a list of all words to which self could be (but has NOT been) applied
        '''
        parents = []
        for parent in Word.objects.filter(pos=self.origin_pos):
            if re.match(self.origin_form, parent.spelling) and not Word.objects.filter(pattern=self, stem=parent):
                parents += [parent]
        return parents

    def __str__(self):
        return self.name
