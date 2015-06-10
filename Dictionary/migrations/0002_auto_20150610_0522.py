# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deriver',
            name='example_stem',
            field=models.ForeignKey(to='Dictionary.Word'),
        ),
    ]
