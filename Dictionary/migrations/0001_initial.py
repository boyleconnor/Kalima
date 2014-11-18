# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deriver',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('origin_pos', models.CharField(max_length=15, choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')])),
                ('result_pos', models.CharField(max_length=15, choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')])),
                ('expectation', models.CharField(max_length=255, default='([اويىبتثجحخدذرزسشصضطظعغفقكلمنهء])([اويىبتثجحخدذرزسشصضطظعغفقكلمنهء])([اويىبتثجحخدذرزسشصضطظعغفقكلمنهء])')),
                ('template', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=63, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('pos', models.CharField(max_length=15, choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')])),
                ('spelling', models.CharField(max_length=255)),
                ('definition', models.TextField()),
                ('examples', models.TextField(blank=True)),
                ('pattern', models.ForeignKey(to='Dictionary.Deriver', related_name='words', null=True, blank=True)),
                ('stem', models.ForeignKey(to='Dictionary.Word', related_name='derivatives', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
