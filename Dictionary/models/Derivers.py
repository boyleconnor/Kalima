from ArabicTools.constants import DEFAULT_ROOT_SPELLING, POS_CHOICES, ABJAD, GENDER_CHOICES
from ArabicTools.utils import pattern_to_form, apply
from Dictionary.models.Words import Word, Adverb, Verb, Adjective, Noun, Root
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, CharField, ForeignKey, BooleanField
from rest_framework.reverse import reverse_lazy


class Deriver(Model):
    class Meta:
        app_label = 'Dictionary'
    result_model = Word
    origin_pos = CharField(max_length=16, choices=POS_CHOICES)
    origin_form = CharField(default=('([%s])' % ABJAD) * 3, max_length=255)
    result_form = CharField(max_length=255)
    origin_pattern = ForeignKey('self', blank=True, null=True, related_name='result_patterns')
    default_root = CharField(max_length=4)
    name = CharField(max_length=63, blank=True)

    def get_origin_form_display(self):
        return pattern_to_form(self.origin_form)

    def get_result_form(self):
        if self.origin_pos == 'root':
            return self.apply(Root(spelling=self.default_root, pos='root'))
        return self.apply(self.origin_pattern.get_result_form())

    def get_result_form_display(self):
        return self.get_result_form().spelling

    def apply_spelling(self, word):
        return apply(self.origin_form, word.spelling, self.result_form)

    def apply(self, stem, save=False, **kwargs):
        result = self.result_model(spelling=self.apply_spelling(stem), stem=stem, pattern=self, **kwargs)
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


class NounDeriver(Deriver):
    result_model = Noun
    gender = CharField(max_length=20, choices=GENDER_CHOICES)
    human = BooleanField(default=False)

    def apply(self, stem, save=False, *args, **kwargs):
        return self.apply(stem, save, gender=self.gender, human=self.human, *args, **kwargs)


class AdjectiveDeriver(Deriver):
    result_model = Adjective

    def apply(self, *args, **kwargs):
        return super(AdjectiveDeriver, self).apply(*args, **kwargs)


class VerbDeriver(Deriver):
    result_model = Verb

    def apply(self, *args, **kwargs):
        return super(VerbDeriver, self).apply(transitive=self.transitive, noun=self.noun, *args, **kwargs)


class AdverbDeriver(Deriver):
    result_model = Adverb