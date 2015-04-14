# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blees', '0002_auto_20150410_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='taken',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
