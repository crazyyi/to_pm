# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20141210_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_edited_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 5, 6, 30, 776553, tzinfo=utc), verbose_name='date last edited'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 5, 6, 30, 776513, tzinfo=utc), verbose_name='date published', auto_now_add=True),
            preserve_default=True,
        ),
    ]
