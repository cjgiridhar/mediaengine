__author__ = 'cgiridhar'
'''
class UserKeyResource(ModelResource):
    user = fields.ForeignKey(UserProfileResource, 'user', null=False, unique=True, full=True)

    class Meta:
        queryset = UserKey.objects.all()
        resource_name = 'userkeys'
        always_return_data = True
        include_resource_uri = False
        allowed_methods = ['post', 'get', 'put']
        authorization = Authorization()
        #cache = SimpleCache(cache_name='resources', timeout=3600, public=True)

    def determine_format(self, request):
        return 'application/json'

    def dehydrate(self, bundle):
        """ Works on GET Requests """
        Utils().show_fields(bundle,'api_key', 'date_created', 'user')
        return bundle

    def alter_list_data_to_serialize(self, request, data_dict):
        """ Works on GET Requests """
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                # Get rid of the "meta".
                del(data_dict['meta'])
                data_dict['userkeys'] = copy.copy(data_dict['objects'])
                del(data_dict['objects'])
        return data_dict

    def obj_create(self, bundle, request=None, **kwargs):
        try:
            user = bundle.data['user']
            if user is None:
                raise BadRequest("User can't be blank!")
        except KeyError as missing_key:
            raise BadRequest("Must provide {missing_key} when creating a user.".format(missing_key=missing_key))
        return super(UserKeyResource, self).obj_create(bundle, **kwargs)

    def determine_format(self, request):
        return 'application/json'



class UserKey(models.Model):
    user = models.ForeignKey(UserProfile, blank=False, null=False, unique=True)
    api_key = models.CharField(max_length=200, blank=False, null=False, unique=True)
    date_created = models.DateTimeField(default=datetime.now(), blank=False)

    def __unicode__(self):
        return unicode(self.user)


class UserKey(models.Model):
    user = models.ForeignKey(UserProfile, blank=False, null=False, unique=True)
    api_key = models.CharField(max_length=200, blank=False, null=False, unique=True)
    date_created = models.DateTimeField(default=datetime.now(), blank=False)

    def __unicode__(self):
        return unicode(self.user)

'''