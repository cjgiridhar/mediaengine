from django.contrib import admin
from user_service.models import UserProfile, UserBilling
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class MyUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name',
                    'is_active')
    ordering = ('-id',)
    search_fields = ('email', 'username')
    list_filter = ('is_active', )
    actions = ['make_activated', 'make_verified']

    def make_activated(self, request, queryset):
        queryset.update(is_active=False)
    make_activated.short_description = "Mark selected user as InActive"




class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'title', 'company', 'status')
    ordering = ('-id',)
    #search_fields = ('email', 'username')
    #list_filter = ('is_active', 'is_verified')
    actions = ['make_verified']

    def make_verified(self, request, queryset):
        queryset.update(is_verified=True)
    make_verified.short_description = "Mark selected user as Verified"


class UserBillingAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'is_plan_active', 'date_created', 'date_updated',
                    'quota_available', 'quota_utilized')
    search_fields = ('user',)
    ordering = ('-id', )
    list_filter = ('is_plan_active', )



admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserBilling, UserBillingAdmin)
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)