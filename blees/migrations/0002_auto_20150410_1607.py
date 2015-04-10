# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='taken',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
