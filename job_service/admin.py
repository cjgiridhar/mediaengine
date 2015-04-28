from django.contrib import admin
from models import JobProfile, AudioSetting, VideoSetting, FrameRate, Resolution
# Register your models here.

class JobProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'audio',
                    'video', 'frame_rate', 'resolution')
    ordering = ('-id',)
    search_fields = ('profile', )

class AudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'audio_codec', 'audio_bitrate',
                    'audio_sample_rate', 'audio_channels')
    ordering = ('-id',)
    search_fields = ('audio_codec', )

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'video_codec', 'video_profile',
                    'video_bitrate', 'video_preset')
    ordering = ('-id',)
    search_fields = ('video_codec', )

class ResolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'width', 'height', 'aspect')
    ordering = ('-id',)
    search_fields = ('aspect', )


class FrameRateAdmin(admin.ModelAdmin):
    list_display = ('id', 'frame_rate', 'key_frame_interval',)
    ordering = ('-id',)
    search_fields = ('frame_rate', )


admin.site.register(JobProfile, JobProfileAdmin)
admin.site.register(AudioSetting, AudioAdmin)
admin.site.register(VideoSetting, VideoAdmin)
admin.site.register(Resolution, ResolutionAdmin)
admin.site.register(FrameRate, FrameRateAdmin)