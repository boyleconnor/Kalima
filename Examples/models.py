from django.db.models import Model, TextField, PositiveSmallIntegerField, ForeignKey
from Inflections.models import Inflection


class Example(Model):
    translation = TextField()

    def get_inflections(self):
        inflections = set()
        for member in self.members.all():
            inflections.add(member.inflection)

    def __str__(self):
        out = []
        for member in self.members.all():
            out.append(member.__str__())
        return ' '.join(out)


class ExampleMember(Model):
    class Meta:
        unique_together = (
            ('position', 'example'),
        )
        order_with_respect_to = 'example'
    example = ForeignKey(Example, related_name='members')
    inflection = ForeignKey(Inflection)
    position = PositiveSmallIntegerField()

    def __str__(self):
        return self.inflection.spelling
