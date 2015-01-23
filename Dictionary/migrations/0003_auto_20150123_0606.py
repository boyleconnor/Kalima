# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dictionary', '0002_auto_20141231_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deriver',
            name='origin_form',
            field=models.CharField(max_length=255, default='xxx'),
            preserve_default=True,
        ),
    ]
