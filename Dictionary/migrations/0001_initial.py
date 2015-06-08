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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('origin_pos', models.CharField(choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')], max_length=16)),
                ('result_pos', models.CharField(choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')], max_length=16)),
                ('origin_form', models.CharField(default='([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])', max_length=255)),
                ('result_form', models.CharField(max_length=255)),
                ('example_stem', models.CharField(blank=True, max_length=4)),
                ('name', models.CharField(blank=True, max_length=63)),
                ('origin_pattern', models.ForeignKey(to='Dictionary.Deriver', null=True, related_name='result_patterns', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inflecter',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('origin_form', models.CharField(max_length=255)),
                ('result_form', models.CharField(max_length=255)),
                ('case', models.CharField(choices=[('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative')], max_length=20, blank=True)),
                ('state', models.CharField(choices=[('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite')], max_length=20, blank=True)),
                ('number', models.CharField(choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')], max_length=20, blank=True)),
                ('gender', models.CharField(choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')], max_length=20, blank=True)),
                ('person', models.CharField(choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')], max_length=20, blank=True)),
                ('tense', models.CharField(choices=[('perfect', 'Perfect'), ('indicative-imperfect', 'Indicative-Imperfect'), ('subjunctive-imperfect', 'Subjunctive-Imperfect'), ('jussive-imperfect', 'Jussive-Imperfect'), ('imperative', 'Imperative')], max_length=20, blank=True)),
                ('voice', models.CharField(choices=[('active', 'Active'), ('passive', 'Passive')], max_length=20, blank=True)),
                ('origin_pattern', models.ForeignKey(to='Dictionary.Deriver')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inflection',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('spelling', models.CharField(max_length=250)),
                ('case', models.CharField(choices=[('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative')], max_length=20, blank=True)),
                ('state', models.CharField(choices=[('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite')], max_length=20, blank=True)),
                ('number', models.CharField(choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')], max_length=20, blank=True)),
                ('gender', models.CharField(choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')], max_length=20, blank=True)),
                ('person', models.CharField(choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')], max_length=20, blank=True)),
                ('tense', models.CharField(choices=[('perfect', 'Perfect'), ('indicative-imperfect', 'Indicative-Imperfect'), ('subjunctive-imperfect', 'Subjunctive-Imperfect'), ('jussive-imperfect', 'Jussive-Imperfect'), ('imperative', 'Imperative')], max_length=20, blank=True)),
                ('voice', models.CharField(choices=[('active', 'Active'), ('passive', 'Passive')], max_length=20, blank=True)),
                ('pattern', models.ForeignKey(to='Dictionary.Inflecter', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('pos', models.CharField(choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')], max_length=20)),
                ('spelling', models.CharField(max_length=255)),
                ('definition', models.TextField(verbose_name='Definition')),
                ('examples', models.TextField(verbose_name='Examples', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('word_ptr', models.OneToOneField(serialize=False, auto_created=True, to='Dictionary.Word', primary_key=True, parent_link=True)),
            ],
            options={
            },
            bases=('Dictionary.word',),
        ),
        migrations.CreateModel(
            name='Root',
            fields=[
                ('word_ptr', models.OneToOneField(serialize=False, auto_created=True, to='Dictionary.Word', primary_key=True, parent_link=True)),
                ('length', models.SmallIntegerField(choices=[(3, 'Three'), (4, 'Four')])),
            ],
            options={
            },
            bases=('Dictionary.word',),
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('word_ptr', models.OneToOneField(serialize=False, auto_created=True, to='Dictionary.Word', primary_key=True, parent_link=True)),
                ('gender', models.CharField(choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')], max_length=20)),
                ('human', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('Dictionary.word',),
        ),
        migrations.CreateModel(
            name='Adverb',
            fields=[
                ('word_ptr', models.OneToOneField(serialize=False, auto_created=True, to='Dictionary.Word', primary_key=True, parent_link=True)),
            ],
            options={
            },
            bases=('Dictionary.word',),
        ),
        migrations.CreateModel(
            name='Adjective',
            fields=[
                ('word_ptr', models.OneToOneField(serialize=False, auto_created=True, to='Dictionary.Word', primary_key=True, parent_link=True)),
                ('noun', models.ManyToManyField(to='Dictionary.Noun')),
            ],
            options={
            },
            bases=('Dictionary.word',),
        ),
        migrations.AddField(
            model_name='word',
            name='pattern',
            field=models.ForeignKey(to='Dictionary.Deriver', null=True, related_name='words', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='word',
            name='stem',
            field=models.ForeignKey(to='Dictionary.Word', null=True, related_name='derivatives', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verb',
            name='noun',
            field=models.ManyToManyField(to='Dictionary.Noun'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inflection',
            name='stem',
            field=models.ForeignKey(to='Dictionary.Word'),
            preserve_default=True,
        ),
    ]
