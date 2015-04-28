from django.conf.urls import patterns, include, url
from django.contrib import admin
from user_service.api import UserProfileResource, UserBillingResource, UserResource
from job_service.api import JobProfileResource, AudioResource, VideoResource, FrameRateResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(UserProfileResource())
v1_api.register(UserResource())
v1_api.register(UserBillingResource())
v1_api.register(JobProfileResource())
v1_api.register(AudioResource())
v1_api.register(VideoResource())
v1_api.register(FrameRateResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mediaengine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
