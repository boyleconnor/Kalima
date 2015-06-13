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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('origin_pos', models.CharField(max_length=16, choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')])),
                ('result_pos', models.CharField(max_length=16, choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')])),
                ('origin_form', models.CharField(max_length=255, default='([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])')),
                ('result_form', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=63, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('pos', models.CharField(max_length=20, choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')])),
                ('spelling', models.CharField(max_length=255)),
                ('definition', models.TextField(verbose_name='Definition')),
                ('examples', models.TextField(verbose_name='Examples', blank=True)),
                ('pattern', models.ForeignKey(to='Dictionary.Deriver', blank=True, null=True, related_name='words')),
                ('stem', models.ForeignKey(to='Dictionary.Word', blank=True, null=True, related_name='derivatives')),
            ],
        ),
        migrations.AddField(
            model_name='deriver',
            name='example_stem',
            field=models.ForeignKey(to='Dictionary.Word', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deriver',
            name='origin_pattern',
            field=models.ForeignKey(to='Dictionary.Deriver', blank=True, null=True, related_name='result_patterns'),
        ),
    ]
