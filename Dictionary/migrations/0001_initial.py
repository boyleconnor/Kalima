# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deriver',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('origin_form', models.CharField(default='([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])([اويىبتثجحخدذرزسشصضطظعغفقكلمنهءة])', max_length=255)),
                ('result_form', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=63)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdverbDeriver',
            fields=[
                ('deriver_ptr', models.OneToOneField(to='Dictionary.Deriver', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=('Dictionary.deriver',),
        ),
        migrations.CreateModel(
            name='AdjectiveDeriver',
            fields=[
                ('deriver_ptr', models.OneToOneField(to='Dictionary.Deriver', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=('Dictionary.deriver',),
        ),
        migrations.CreateModel(
            name='Inflecter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('origin_form', models.CharField(max_length=255)),
                ('result_form', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conjugator',
            fields=[
                ('inflecter_ptr', models.OneToOneField(to='Dictionary.Inflecter', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('number', models.CharField(blank=True, choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')], max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')], max_length=20)),
                ('person', models.CharField(blank=True, choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')], max_length=20)),
                ('tense', models.CharField(blank=True, choices=[('perfect', 'Perfect'), ('indicative-imperfect', 'Indicative-Imperfect'), ('subjunctive-imperfect', 'Subjunctive-Imperfect'), ('jussive-imperfect', 'Jussive-Imperfect'), ('imperative', 'Imperative')], max_length=20)),
                ('voice', models.CharField(blank=True, choices=[('active', 'Active'), ('passive', 'Passive')], max_length=20)),
            ],
            options={
            },
            bases=('Dictionary.inflecter',),
        ),
        migrations.CreateModel(
            name='AdjectiveDecliner',
            fields=[
                ('inflecter_ptr', models.OneToOneField(to='Dictionary.Inflecter', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('case', models.CharField(blank=True, choices=[('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative')], max_length=20)),
                ('number', models.CharField(blank=True, choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')], max_length=20)),
                ('state', models.CharField(blank=True, choices=[('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite')], max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')], max_length=20)),
            ],
            options={
            },
            bases=('Dictionary.inflecter',),
        ),
        migrations.CreateModel(
            name='Inflection',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('spelling', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conjugation',
            fields=[
                ('inflection_ptr', models.OneToOneField(to='Dictionary.Inflection', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('number', models.CharField(blank=True, choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')], max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')], max_length=20)),
                ('person', models.CharField(blank=True, choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')], max_length=20)),
                ('tense', models.CharField(blank=True, choices=[('perfect', 'Perfect'), ('indicative-imperfect', 'Indicative-Imperfect'), ('subjunctive-imperfect', 'Subjunctive-Imperfect'), ('jussive-imperfect', 'Jussive-Imperfect'), ('imperative', 'Imperative')], max_length=20)),
                ('voice', models.CharField(blank=True, choices=[('active', 'Active'), ('passive', 'Passive')], max_length=20)),
            ],
            options={
            },
            bases=('Dictionary.inflection',),
        ),
        migrations.CreateModel(
            name='AdjectiveDeclension',
            fields=[
                ('inflection_ptr', models.OneToOneField(to='Dictionary.Inflection', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('case', models.CharField(blank=True, choices=[('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative')], max_length=20)),
                ('number', models.CharField(blank=True, choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')], max_length=20)),
                ('state', models.CharField(blank=True, choices=[('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite')], max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')], max_length=20)),
            ],
            options={
            },
            bases=('Dictionary.inflection',),
        ),
        migrations.CreateModel(
            name='NounDeclension',
            fields=[
                ('inflection_ptr', models.OneToOneField(to='Dictionary.Inflection', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('case', models.CharField(blank=True, choices=[('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative')], max_length=20)),
                ('number', models.CharField(blank=True, choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')], max_length=20)),
                ('state', models.CharField(blank=True, choices=[('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite')], max_length=20)),
            ],
            options={
            },
            bases=('Dictionary.inflection',),
        ),
        migrations.CreateModel(
            name='NounDecliner',
            fields=[
                ('inflecter_ptr', models.OneToOneField(to='Dictionary.Inflecter', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('case', models.CharField(blank=True, choices=[('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative')], max_length=20)),
                ('number', models.CharField(blank=True, choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')], max_length=20)),
                ('state', models.CharField(blank=True, choices=[('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite')], max_length=20)),
            ],
            options={
            },
            bases=('Dictionary.inflecter',),
        ),
        migrations.CreateModel(
            name='NounDeriver',
            fields=[
                ('deriver_ptr', models.OneToOneField(to='Dictionary.Deriver', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('gender', models.CharField(choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')], max_length=20)),
                ('human', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('Dictionary.deriver',),
        ),
        migrations.CreateModel(
            name='VerbDeriver',
            fields=[
                ('deriver_ptr', models.OneToOneField(to='Dictionary.Deriver', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=('Dictionary.deriver',),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('pos', models.CharField(choices=[('noun', 'Noun'), ('verb', 'Verb'), ('adjective', 'Adjective'), ('preposition', 'Preposition'), ('root', 'Root')], max_length=20)),
                ('spelling', models.CharField(max_length=255)),
                ('definition', models.TextField(verbose_name='Definition')),
                ('examples', models.TextField(blank=True, verbose_name='Examples')),
                ('tags', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('word_ptr', models.OneToOneField(to='Dictionary.Word', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=('Dictionary.word',),
        ),
        migrations.CreateModel(
            name='Root',
            fields=[
                ('word_ptr', models.OneToOneField(to='Dictionary.Word', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('length', models.SmallIntegerField(choices=[(3, 'three'), (4, 'four')])),
            ],
            options={
            },
            bases=('Dictionary.word',),
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('word_ptr', models.OneToOneField(to='Dictionary.Word', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
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
                ('word_ptr', models.OneToOneField(to='Dictionary.Word', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=('Dictionary.word',),
        ),
        migrations.CreateModel(
            name='Adjective',
            fields=[
                ('word_ptr', models.OneToOneField(to='Dictionary.Word', parent_link=True, primary_key=True, serialize=False, auto_created=True)),
                ('noun', models.ManyToManyField(to='Dictionary.Noun')),
            ],
            options={
            },
            bases=('Dictionary.word',),
        ),
        migrations.AddField(
            model_name='word',
            name='pattern',
            field=models.ForeignKey(blank=True, null=True, related_name='words', to='Dictionary.Deriver'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='word',
            name='stem',
            field=models.ForeignKey(blank=True, null=True, related_name='derivatives', to='Dictionary.Word'),
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
            name='pattern',
            field=models.ForeignKey(to='Dictionary.Inflecter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inflection',
            name='stem',
            field=models.ForeignKey(to='Dictionary.Word'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inflecter',
            name='origin_pattern',
            field=models.ForeignKey(to='Dictionary.Deriver'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deriver',
            name='origin_pattern',
            field=models.ForeignKey(blank=True, null=True, related_name='result_patterns', to='Dictionary.Deriver'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deriver',
            name='origin_pos',
            field=models.ForeignKey(max_length=15, to='contenttypes.ContentType'),
            preserve_default=True,
        ),
    ]
