# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_pos', models.CharField(choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')], max_length=16)),
                ('result_pos', models.CharField(choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')], max_length=16)),
                ('origin_form', models.CharField(default='([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])', max_length=255)),
                ('result_form', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')], max_length=20)),
                ('spelling', models.CharField(max_length=255)),
                ('definition', models.TextField(verbose_name='Definition')),
                ('examples', models.TextField(blank=True, verbose_name='Examples')),
                ('pattern', models.ForeignKey(null=True, to='Dictionary.Pattern', related_name='words', blank=True)),
                ('stem', models.ForeignKey(null=True, to='Dictionary.Word', related_name='derivatives', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='pattern',
            name='example_stem',
            field=models.ForeignKey(null=True, to='Dictionary.Word', related_name='example_in', blank=True),
        ),
        migrations.AddField(
            model_name='pattern',
            name='origin_pattern',
            field=models.ForeignKey(null=True, to='Dictionary.Pattern', related_name='result_patterns', blank=True),
        ),
    ]
