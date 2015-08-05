from ArabicTools.mixins import AttributesMixin, AbstractPattern, Spellable
from ArabicTools.utils import validate_inflection_attributes, validate_stem_attributes
from django.db.models import Model, ForeignKey, CharField
from django.db.models.fields.related import OneToOneField


class Inflection(AttributesMixin, Spellable):
    stem = ForeignKey('Inflections.Stem', blank=True, null=True)
    pattern = ForeignKey('Inflections.Inflecter', blank=True, null=True)

    def clean(self):
        validate_inflection_attributes(self.stem.parent.pos, self.attributes)


class Stem(AttributesMixin, Spellable):
    parent = ForeignKey('Dictionary.Word')
    pattern = ForeignKey('Inflections.Stemmer', blank=True, null=True)
    exemplar = OneToOneField('Inflections.Inflection', related_name='exemplar_of', null=True)

    def clean(self):
        validate_stem_attributes(self.parent.pos, self.attributes)


class Stemmer(AttributesMixin, AbstractPattern):
    origin_pattern = ForeignKey('Dictionary.Pattern', blank=True, null=True)

    class Meta:
        order_with_respect_to = 'origin_pattern'
    result_model = Stem

    def clean(self):
        validate_stem_attributes(self.origin_pattern.result_pos, self.attributes)

    def apply(self, *args, **kwargs):
        return super(Stemmer, self).apply(attributes=self.attributes, *args, **kwargs)


class Paradigm(Model):
    name = CharField(max_length=100)


class Inflecter(AttributesMixin):
    result_model = Inflection
    paradigm = ForeignKey(Paradigm, null=True)
    prefix = CharField(max_length=10, blank=True)
    suffix = CharField(max_length=10, blank=True)

    def generate_spelling(self, spelling):
        return self.prefix + spelling + self.suffix

    def apply(self, stem, save=False, *args, **kwargs):
        if Inflection.objects.filter(stem=stem, pattern=self): raise ValueError('Inflection with given stem and pattern already exists')
        result = Inflection(attributes=self.attributes, spelling=self.generate_spelling(stem.spelling), stem=stem, pattern=self, *args, **kwargs)
        if save:
            result.save()
        return result

    def apply_to_best_stem(self, word, save=False):
        for stem in word.stem_set.all():
            if self.attributes_match(stem):
                return self.apply(stem, save=save)

    def attributes_match(self, stem):
        stem_attributes = stem.get_attributes()
        stem_is_bad = False
        for attribute in stem_attributes:
            if self.get_attributes()[attribute] not in stem_attributes[attribute].split('/'):
                stem_is_bad = True
                break
        if not stem_is_bad:
            return True

    def __str__(self):
        return '%s %s' % (self.prefix, self.suffix)
