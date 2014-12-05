# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 15, 12, 3, 290114, tzinfo=utc), verbose_name='date published', auto_now_add=True),
            preserve_default=True,
        ),
    ]
