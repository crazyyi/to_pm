# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20141204_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2014, 12, 4, 6, 47, 16, 744330, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
