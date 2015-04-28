from django.db import models
from django.contrib.auth.models import User
from user_service.models import UserProfile
from datetime import datetime
# Create your models here.
from user_service.enum import transcode_error_codes, progress_codes, \
    phase_codes, notification_codes, error_levels, job_priority_levels

class VideoSetting(models.Model):
    #name = models.CharField(max_length=50, blank=False, null=False, default='libx264_baseline_512000_ultrafast')
    video_codec = models.CharField(max_length=10, default='libx264', blank=False, null=False)
    video_profile = models.CharField(max_length=100, blank=False, null=False, default='baseline')
    video_bitrate = models.IntegerField(default=512000, blank=False, null=False)
    video_preset = models.CharField(max_length=15, default='ultrafast', blank=False, null=False)

    def __unicode__(self):
        return unicode(self.pk)

class AudioSetting(models.Model):
    #name = models.CharField(max_length=50, blank=False, null=False, default='libfdk_aac_128000_44100_2')
    audio_codec = models.CharField(max_length=10, default='libfdk_aac', blank=False, null=False)
    audio_bitrate = models.IntegerField(default=128000, blank=False, null=False)
    audio_sample_rate = models.IntegerField(default=44100, blank=False, null=False)
    audio_channels = models.IntegerField(default=2, blank=False, null=False)

    def __unicode__(self):
        return unicode(self.pk)


class Resolution(models.Model):
    #name = models.CharField(max_length=50, blank=False, null=False, default='1280_720_4:3')
    width = models.IntegerField(default=1280, blank=False, null=False)
    height = models.IntegerField(default=720, blank=False, null=False)
    aspect = models.CharField(max_length=5, default='4:3', blank=False, null=False)

    def __unicode__(self):
        return unicode(self.pk)


class FrameRate(models.Model):
    #name = models.CharField(max_length=50, blank=False, null=False, default='30_180')
    frame_rate = models.IntegerField(null=False, blank=False, default=30)
    key_frame_interval = models.IntegerField(null=False, blank=False, default=180)

    def __unicode__(self):
        return unicode(self.pk)


class Error(models.Model):
    code = models.IntegerField(choices=transcode_error_codes, null=True, blank=False)
    description = models.CharField(max_length=200, blank=False, null=False, default='Unknown')
    level = models.IntegerField(choices=error_levels, default=0)


class JobProfile(models.Model):
    user = models.OneToOneField(User, null=False, blank=False)
    #name = models.CharField(max_length=30, null=False, blank=False)
    audio = models.ForeignKey(AudioSetting, null=False, blank=False)
    video = models.ForeignKey(VideoSetting, null=False, blank=False)
    resolution = models.ForeignKey(Resolution, null=False, blank=False)
    frame_rate = models.ForeignKey(FrameRate, null=False, blank=False)

    def __unicode__(self):
        return unicode(self.pk)


class JobProgress(models.Model):
    state = models.CharField(max_length=50, choices=progress_codes,
        default='PENDING', null=False, blank=False)
    current_phase = models.CharField(max_length=100, choices=phase_codes,
        default='', null=False, blank=False)
    current_phase_progress = models.FloatField(max_length=20, default=0.0)
    overall_job_progress = models.FloatField(max_length=20, default=0.0)

class Input(models.Model):
    url = models.CharField(max_length=50, null=False, blank=False, default='')
    file_format = models.CharField(max_length=10, null=False, blank=False, default='')
    file_size = models.IntegerField(max_length=10, default=0, null=False, blank=False)
    duration = models.IntegerField(max_length=10, default=0, null=False, blank=True)
    sha1_hash = models.CharField(max_length=32, null=True, blank=False, default='')

class Output(models.Model):
    url = models.CharField(max_length=50, null=False, blank=False, default='')
    file_format = models.CharField(max_length=10, null=False, blank=False, default='')
    file_size = models.IntegerField(max_length=10, default=0, null=False, blank=False)
    duration = models.IntegerField(max_length=10, default=0, null=False, blank=True)
    sha1_hash = models.CharField(max_length=32, null=True, blank=False, default='')

class Job(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    profile = models.ForeignKey(JobProfile, null=False, blank=False)
    input = models.ForeignKey(Input, null=False, blank=False)
    output = models.ForeignKey(Output, null=False, blank=False)
    progress = models.ForeignKey(JobProgress, null=False, blank=False)
    priority = models.CharField(max_length=6, choices=job_priority_levels, default='LOW', null=False, blank=False)
    notification = models.CharField(max_length=10, choices=notification_codes, default='EMAIL',)
    date_submitted = models.DateTimeField(default=datetime.now(), blank=False, null=False)
    date_updated = models.DateTimeField(blank=False, null=True)
    date_finished = models.DateTimeField(blank=False, null=True)

