# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dictionary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inflecter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('origin_form', models.CharField(max_length=255)),
                ('result_form', models.CharField(max_length=255)),
                ('case', models.CharField(max_length=20, blank=True, choices=[('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative')])),
                ('state', models.CharField(max_length=20, blank=True, choices=[('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite')])),
                ('number', models.CharField(max_length=20, blank=True, choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')])),
                ('gender', models.CharField(max_length=20, blank=True, choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')])),
                ('person', models.CharField(max_length=20, blank=True, choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')])),
                ('tense', models.CharField(max_length=20, blank=True, choices=[('perfect', 'Perfect'), ('indicative-imperfect', 'Indicative-Imperfect'), ('subjunctive-imperfect', 'Subjunctive-Imperfect'), ('jussive-imperfect', 'Jussive-Imperfect'), ('imperative', 'Imperative')])),
                ('voice', models.CharField(max_length=20, blank=True, choices=[('active', 'Active'), ('passive', 'Passive')])),
                ('origin_pattern', models.ForeignKey(to='Dictionary.Deriver')),
            ],
        ),
        migrations.CreateModel(
            name='Inflection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('spelling', models.CharField(max_length=250)),
                ('attributes', models.TextField()),
                ('case', models.CharField(max_length=20, blank=True, choices=[('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative')])),
                ('state', models.CharField(max_length=20, blank=True, choices=[('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite')])),
                ('number', models.CharField(max_length=20, blank=True, choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')])),
                ('gender', models.CharField(max_length=20, blank=True, choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')])),
                ('person', models.CharField(max_length=20, blank=True, choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')])),
                ('tense', models.CharField(max_length=20, blank=True, choices=[('perfect', 'Perfect'), ('indicative-imperfect', 'Indicative-Imperfect'), ('subjunctive-imperfect', 'Subjunctive-Imperfect'), ('jussive-imperfect', 'Jussive-Imperfect'), ('imperative', 'Imperative')])),
                ('voice', models.CharField(max_length=20, blank=True, choices=[('active', 'Active'), ('passive', 'Passive')])),
                ('pattern', models.ForeignKey(to='Inflections.Inflecter', blank=True, null=True)),
                ('stem', models.ForeignKey(to='Dictionary.Word')),
            ],
        ),
    ]
