# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_auto_20141210_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_edited_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 7, 10, 57, 849442, tzinfo=utc), verbose_name='date last edited'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published', default=datetime.datetime(2014, 12, 10, 7, 10, 57, 849400, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
