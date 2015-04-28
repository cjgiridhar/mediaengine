# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('audio_codec', models.CharField(default=b'libfdk_aac', max_length=10)),
                ('audio_bitrate', models.IntegerField(default=128000)),
                ('audio_sample_rate', models.IntegerField(default=44100)),
                ('audio_channels', models.IntegerField(default=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(null=True, choices=[(0, b'Success'), (1, b'Input_File_Not_Found')])),
                ('description', models.CharField(default=b'Unknown', max_length=200)),
                ('level', models.IntegerField(default=0, choices=[(b'Info', 0), (b'Warning', 1), (b'Critical', 2)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FrameRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('frame_rate', models.IntegerField(default=30)),
                ('key_frame_interval', models.IntegerField(default=180)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=b'', max_length=50)),
                ('file_format', models.CharField(default=b'', max_length=10)),
                ('file_size', models.IntegerField(default=0, max_length=10)),
                ('duration', models.IntegerField(default=0, max_length=10, blank=True)),
                ('sha1_hash', models.CharField(default=b'', max_length=32, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.CharField(default=b'LOW', max_length=6, choices=[(b'HIGH', 'High'), (b'MEDIUM', 'Medium'), (b'LOW', 'Low')])),
                ('notification', models.CharField(default=b'EMAIL', max_length=10, choices=[(b'EMAIL', 'Email'), (b'SMS', 'Sms')])),
                ('date_submitted', models.DateTimeField(default=datetime.datetime(2015, 4, 20, 12, 45, 52, 237762))),
                ('date_updated', models.DateTimeField(null=True)),
                ('date_finished', models.DateTimeField(null=True)),
                ('input', models.ForeignKey(to='job_service.Input')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('audio', models.ForeignKey(to='job_service.AudioSetting')),
                ('frame_rate', models.ForeignKey(to='job_service.FrameRate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(default=b'PENDING', max_length=50, choices=[(b'PENDING', 'Pending'), (b'QUEUED', 'Queued'), (b'INPROGRESS', 'InProgress'), (b'COMPLETED', 'Completed'), (b'CANCELLED', 'Cancelled'), (b'FAILED', 'Failed')])),
                ('current_phase', models.CharField(default=b'', max_length=100, choices=[(b'DOWNLOAD', 'Download'), (b'TRANSCODE', 'Transcode'), (b'THUMBNAIL', 'Thumbnail'), (b'SPRITE', 'Sprite'), (b'UPLOAD', 'Upload')])),
                ('current_phase_progress', models.FloatField(default=0.0, max_length=20)),
                ('overall_job_progress', models.FloatField(default=0.0, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=b'', max_length=50)),
                ('file_format', models.CharField(default=b'', max_length=10)),
                ('file_size', models.IntegerField(default=0, max_length=10)),
                ('duration', models.IntegerField(default=0, max_length=10, blank=True)),
                ('sha1_hash', models.CharField(default=b'', max_length=32, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.IntegerField(default=1280)),
                ('height', models.IntegerField(default=720)),
                ('aspect', models.CharField(default=b'4:3', max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video_codec', models.CharField(default=b'libx264', max_length=10)),
                ('video_profile', models.CharField(default=b'baseline', max_length=100)),
                ('video_bitrate', models.IntegerField(default=512000)),
                ('video_preset', models.CharField(default=b'ultrafast', max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='jobprofile',
            name='resolution',
            field=models.ForeignKey(to='job_service.Resolution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobprofile',
            name='video',
            field=models.ForeignKey(to='job_service.VideoSetting'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='output',
            field=models.ForeignKey(to='job_service.Output'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='profile',
            field=models.ForeignKey(to='job_service.JobProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='progress',
            field=models.ForeignKey(to='job_service.JobProgress'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
