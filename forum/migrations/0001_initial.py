# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=120)),
                ('content', models.TextField(verbose_name='Content', max_length=4000)),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime(2014, 12, 3, 15, 9, 23, 185658, tzinfo=utc), auto_now_add=True)),
                ('tag', models.CharField(verbose_name='Tag', max_length=20)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('thread_post', models.ForeignKey(blank=True, null=True, to='forum.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('avator', models.ImageField(blank=True, upload_to='profile_image')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
