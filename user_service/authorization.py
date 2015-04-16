__author__ = 'cgiridhar'
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from user_service.models import UserProfile

class UserObjectsOnlyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        print "OBJECT LIST" + str(object_list)
        return object_list.filter(username=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.username == bundle.request.user

    def create_list(self, object_list, bundle):
        # Assuming they're auto-assigned to ``user``.
        return object_list

    def create_detail(self, object_list, bundle):
        print "USER IS:" + str(bundle.request.user)
        return bundle.obj.username == bundle.request.user

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.username == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")



class EnterpriseObjectsAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        data = UserProfile.objects.filter(username=bundle.request.user)
        return object_list.filter(name=data[0].enterprise)
    

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        print "BUNDLE IS " + str(bundle.obj)
        return bundle.obj.name == bundle.request.name

    # def create_list(self, object_list, bundle):
    #     # Assuming they're auto-assigned to ``user``.
    #     return object_list
    #
    # def create_detail(self, object_list, bundle):
    #     return bundle.obj.username == bundle.request.user

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.username == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")