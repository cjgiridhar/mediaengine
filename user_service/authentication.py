__author__ = 'cgiridhar'
from tastypie.authentication import ApiKeyAuthentication
from user_service.models import UserProfile

class XApiKeyAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        api_key = request.META.get('x_api_key')
        print "HERE" + str(api_key)

        if not api_key:
            return self._unauthorized()
        try:
            user = UserProfile.objects.filter(x_api_key=api_key)
        except (UserProfile.DoesNotExist, UserProfile.MultipleObjectsReturned):
            return self._unauthorized()
        request.user = user
        return self.get_key(user, api_key)