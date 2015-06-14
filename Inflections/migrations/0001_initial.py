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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_form', models.CharField(max_length=255)),
                ('result_form', models.CharField(max_length=255)),
                ('case', models.CharField(choices=[('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative')], blank=True, max_length=20)),
                ('state', models.CharField(choices=[('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite')], blank=True, max_length=20)),
                ('number', models.CharField(choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')], blank=True, max_length=20)),
                ('gender', models.CharField(choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')], blank=True, max_length=20)),
                ('person', models.CharField(choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')], blank=True, max_length=20)),
                ('tense', models.CharField(choices=[('perfect', 'Perfect'), ('indicative-imperfect', 'Indicative-Imperfect'), ('subjunctive-imperfect', 'Subjunctive-Imperfect'), ('jussive-imperfect', 'Jussive-Imperfect'), ('imperative', 'Imperative')], blank=True, max_length=20)),
                ('voice', models.CharField(choices=[('active', 'Active'), ('passive', 'Passive')], blank=True, max_length=20)),
                ('origin_pattern', models.ForeignKey(to='Dictionary.Pattern')),
            ],
        ),
        migrations.CreateModel(
            name='Inflection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling', models.CharField(max_length=250)),
                ('attributes', models.TextField()),
                ('case', models.CharField(choices=[('nominative', 'Nominative'), ('genitive', 'Genitive'), ('accusative', 'Accusative')], blank=True, max_length=20)),
                ('state', models.CharField(choices=[('construct', 'Construct'), ('definite', 'Definite'), ('indefinite', 'Indefinite')], blank=True, max_length=20)),
                ('number', models.CharField(choices=[('singular', 'Singular'), ('dual', 'Dual'), ('plural', 'Plural')], blank=True, max_length=20)),
                ('gender', models.CharField(choices=[('masculine', 'Masculine'), ('feminine', 'Feminine')], blank=True, max_length=20)),
                ('person', models.CharField(choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third')], blank=True, max_length=20)),
                ('tense', models.CharField(choices=[('perfect', 'Perfect'), ('indicative-imperfect', 'Indicative-Imperfect'), ('subjunctive-imperfect', 'Subjunctive-Imperfect'), ('jussive-imperfect', 'Jussive-Imperfect'), ('imperative', 'Imperative')], blank=True, max_length=20)),
                ('voice', models.CharField(choices=[('active', 'Active'), ('passive', 'Passive')], blank=True, max_length=20)),
                ('pattern', models.ForeignKey(null=True, to='Inflections.Inflecter', blank=True)),
                ('stem', models.ForeignKey(to='Dictionary.Word')),
            ],
        ),
    ]
