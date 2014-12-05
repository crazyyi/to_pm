# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20141204_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', auto_now_add=True, default=datetime.datetime(2014, 12, 4, 5, 2, 56, 433316, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
