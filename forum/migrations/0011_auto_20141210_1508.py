# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20141210_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is active'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='last_edited_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 7, 8, 44, 133625, tzinfo=utc), verbose_name='date last edited'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 10, 7, 8, 44, 133584, tzinfo=utc), verbose_name='date published', auto_now_add=True),
            preserve_default=True,
        ),
    ]
