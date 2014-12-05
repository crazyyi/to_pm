# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20141203_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=5000, verbose_name='Content'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published', default=datetime.datetime(2014, 12, 4, 3, 33, 15, 399807, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
