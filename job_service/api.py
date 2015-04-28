__author__ = 'cgiridhar'

from django.contrib.auth.models import User
from job_service.models import JobProfile, AudioSetting, VideoSetting, FrameRate, Resolution
from user_service.api import UserResource
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import Authentication, ApiKeyAuthentication, MultiAuthentication
#from authorization import UserObjectsOnlyAuthorization, EnterpriseObjectsAuthorization
from tastypie.models import create_api_key
from django.db import models
models.signals.post_save.connect(create_api_key, sender=User)
import copy

from tastypie.http import HttpResponse
from tastypie.cache import SimpleCache
from tastypie import fields
from tastypie.exceptions import BadRequest
import json
from utils import Utils


class AudioResource(ModelResource):
    class Meta:
        queryset = AudioSetting.objects.all()
        resource_name = 'audio_setting'
        include_resource_uri = False
        always_return_data = True
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()

    def dehydrate(self, bundle):
        return bundle

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict['audio_setting'] = copy.copy(data_dict['objects'])
                del(data_dict['objects'])
        return data_dict


class VideoResource(ModelResource):
    class Meta:
        queryset = VideoSetting.objects.all()
        resource_name = 'video_setting'
        include_resource_uri = False
        always_return_data = True
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()

    def dehydrate(self, bundle):
        return bundle

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict['video_setting'] = copy.copy(data_dict['objects'])
                del(data_dict['objects'])
        return data_dict

class ResolutionResource(ModelResource):
    class Meta:
        queryset = Resolution.objects.all()
        resource_name = 'resolution'
        include_resource_uri = False
        always_return_data = True
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()

    def dehydrate(self, bundle):
        return bundle

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict['frame_rate'] = copy.copy(data_dict['objects'])
                del(data_dict['objects'])
        return data_dict


class FrameRateResource(ModelResource):
    class Meta:
        queryset = FrameRate.objects.all()
        resource_name = 'frame_rate'
        include_resource_uri = False
        always_return_data = True
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()

    def dehydrate(self, bundle):
        return bundle

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict['frame_rate'] = copy.copy(data_dict['objects'])
                del(data_dict['objects'])
        return data_dict

class JobProfileResource(ModelResource):
    audio = fields.ForeignKey(AudioResource, 'audio', null=True, full=True)
    video = fields.ForeignKey(VideoResource, 'video', null=True, full=True)
    frame_rate = fields.ForeignKey(FrameRateResource, 'frame_rate', null=True, full=True)
    resolution = fields.ForeignKey(ResolutionResource, 'resolution', null=True, full=True)

    class Meta:
        queryset = JobProfile.objects.all()
        resource_name = 'profiles'
        include_resource_uri = False
        always_return_data = True
        allowed_methods = ['get', 'post', 'put']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()

    def dehydrate(self, bundle):
        Utils().show_fields(bundle, 'id', 'audio', 'video', 'frame_rate', 'resolution')
        return bundle

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del(data_dict['meta'])
                data_dict['profiles'] = copy.copy(data_dict['objects'])
                del(data_dict['objects'])
        return data_dict

    def obj_create(self, bundle, request=None, **kwargs):
        try:
            email = bundle.data['email']
            username = bundle.data['username']
            if email is None:
                raise BadRequest("user can't be blank!")
            if email and User.objects.filter(email=email).count() > 0:
                raise BadRequest("email should be unique!")
            if username and User.objects.filter(username=username).count() > 0:
                raise BadRequest("username should be unique!")

        except KeyError as missing_key:
            raise BadRequest("Must provide {missing_key} when creating an enterprise.".format(missing_key=missing_key))
        return super(JobProfileResource, self).obj_create(bundle, **kwargs)