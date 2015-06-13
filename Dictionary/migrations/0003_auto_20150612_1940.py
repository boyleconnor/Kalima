# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dictionary', '0002_auto_20150610_0522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inflecter',
            name='origin_pattern',
        ),
        migrations.RemoveField(
            model_name='inflection',
            name='pattern',
        ),
        migrations.RemoveField(
            model_name='inflection',
            name='stem',
        ),
        migrations.AlterField(
            model_name='deriver',
            name='example_stem',
            field=models.ForeignKey(null=True, to='Dictionary.Word', blank=True),
        ),
        migrations.DeleteModel(
            name='Inflecter',
        ),
        migrations.DeleteModel(
            name='Inflection',
        ),
    ]
