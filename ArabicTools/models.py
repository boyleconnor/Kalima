from django.db.models import Model, CharField, ForeignKey


class SpecialSet(Model):
    name = CharField(max_length=32)

    def get_specials(self):
        specials = {}
        for special in self.specials.all():
            specials[special.key] = special.value
        return specials


class Special(Model):
    class Meta:
        unique_together = (
            ('key', 'special_set')
        )
    special_set = ForeignKey(SpecialSet, related_name='specials')
    key = CharField(max_length=1)
    value = CharField(max_length=4096)
