# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dictionary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deriver',
            old_name='template',
            new_name='result_form',
        ),
        migrations.RemoveField(
            model_name='deriver',
            name='expectation',
        ),
        migrations.AddField(
            model_name='deriver',
            name='origin_form',
            field=models.CharField(max_length=255, default='123'),
            preserve_default=True,
        ),
    ]
