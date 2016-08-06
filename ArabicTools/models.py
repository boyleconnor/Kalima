from django.db.models import Model, CharField, ForeignKey


class SpecialSet(Model):
    '''Dictionary-esque concept that stores the 'special' characters in an
    Arabic style word form.

    e.g. the template [fa3ala -> ifti3aal] is done with the 'special'
    key characters 'f', '3' and 'l', each one containing a value equal to a
    regex pattern matching all sound letters.
    '''
    name = CharField(max_length=32)

    def get_specials(self):
        specials = {}
        for special in self.specials.all():
            specials[special.key] = special.value
        return specials

    def __str__(self):
        return self.name


class Special(Model):
    '''An individual key-value pair of a 'special' character (the key) and the
    characters that can fit its slot in a template.
    '''
    class Meta:
        unique_together = (
            ('key', 'special_set')
        )
    special_set = ForeignKey(SpecialSet, related_name='specials')
    key = CharField(max_length=1)
    value = CharField(max_length=4096)
