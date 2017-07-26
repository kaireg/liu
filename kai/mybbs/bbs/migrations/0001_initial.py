# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bbs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=256, blank=True)),
                ('content', models.TextField()),
                ('view_count', models.IntegerField()),
                ('ranking', models.IntegerField()),
                ('createdtime', models.DateTimeField()),
                ('updatetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='bbs_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('singnature', models.CharField(default=b'this guy is too lazy to levave anything here.', max_length=128)),
                ('photo', models.ImageField(default=b'upload_imgs/user_1.jpg', upload_to=b'upload_imgs/')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('admin', models.ForeignKey(to='bbs.bbs_user')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='bbs',
            name='author',
            field=models.ForeignKey(to='bbs.bbs_user'),
        ),
    ]
