# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import ckeditor.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20141210_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='内容', max_length=5000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='last_edited_date',
            field=models.DateTimeField(verbose_name='date last edited', default=datetime.datetime(2014, 12, 10, 5, 25, 19, 730254, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(verbose_name='喜欢', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published', default=datetime.datetime(2014, 12, 10, 5, 25, 19, 730186, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='标签', through='taggit.TaggedItem', to='taggit.Tag', help_text='A comma-separated list of tags.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=120),
            preserve_default=True,
        ),
    ]
