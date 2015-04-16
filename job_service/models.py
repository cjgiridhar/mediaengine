from django.db import models
from user_service.models import UserProfile
from datetime import datetime
# Create your models here.
import errorcodes

class Video(models.Model):
    video_codec = models.CharField(max_length=10, default='h264', blank=False, null=False)
    video_profile = models.CharField(max_length=100, blank=False, null=False, default='baseline')
    video_bitrate = models.IntegerField(default=512, blank=False, null=False)
    video_preset = models.CharField(max_length=15, default='ultrafast', blank=False, null=False)

class Audio(models.Model):
    audio_codec = models.CharField(max_length=10, default='h264', blank=False, null=False)
    audio_bitrate = models.IntegerField(default=128, blank=False, null=False)
    audio_sample_rate = models.IntegerField(default=44100, blank=False, null=False)
    audio_channels = models.IntegerField(default=2, blank=False, null=False)

class Resolution(models.Model):
    width = models.IntegerField(default=1280, blank=False, null=False)
    height = models.IntegerField(default=720, blank=False, null=False)
    aspect = models.CharField(max_length=5, default='4:3', blank=False, null=False )

class FrameRate(models.Model):
    frame_rate = models.IntegerField(null=False, blank=False, default=30)
    key_frame_interval = models.IntegerField(null=False, blank=False, default=180)

class Error(models.Model):
    code = models.IntegerField(choices=errorcodes.ERROR_CODES, null=True, blank=False)
    description = models.CharField(max_length=200, blank=False, null=False, default='Unknown')
    level = models.IntegerField(choices=(('Info', 0), ('Warning', 1), ('Critical', 2)), default=0)


class Progress(models.Model):
    state = models.CharField(max_length=50, choices=(
        ('Pending', 0), ('Queued', 1), ('InProgress', 2),
        ('Completed', 3), ('Cancelled', 4), ('Failed', 5),),
        default='Pending', null=False, blank=False)
    current_phase = models.CharField(max_length=100, choices=(
        ('Downloading', 0), ('Uploading', 1), ('Transcoding', 0),),
        default='Downloading', null=False, blank=False)
    current_phase_progress = models.FloatField(max_length=20, default=0.0)
    overall_job_progress = models.FloatField(max_length=20, default=0.0)

class Job(models.Model):
    user = models.ForeignKey(UserProfile, null=False, blank=False)
    progress = models.ForeignKey(Progress, null=False, blank=False)

    input = models.CharField(max_length=250, blank=False, null=False)
    output = models.CharField(max_length=250, blank=True, null=True, default='')
    profile = models.CharField(max_length=100, blank=False, null=False, default='default')
    priority = models.IntegerField(blank=False, default=0)
    notification = models.CharField(max_length=10, choices=(('Email', 0), ('SMS', 1),), default='Email',)
    date_submitted = models.DateTimeField(default=datetime.now(), blank=False, null=False)
    date_updated = models.DateTimeField(blank=False, null=True)
    date_finished = models.DateTimeField(blank=False, null=True)

