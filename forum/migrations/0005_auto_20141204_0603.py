# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20141204_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 12, 4, 6, 3, 52, 45088, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
    ]
