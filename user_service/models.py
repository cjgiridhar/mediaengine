from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import enum

# Create your models here.


class UserBilling(models.Model):
    user = models.ForeignKey(User, unique=True)
    plan = models.CharField(max_length=10, choices=enum.user_billing_plan_choices, default='FREE',)
    is_plan_active = models.BooleanField(default=False, blank=False)
    date_created = models.DateTimeField(default=datetime.now(), blank=False)
    date_updated = models.DateTimeField(default=datetime.now(), blank=True)
    quota_available = models.IntegerField(default=0, blank=False)
    quota_utilized = models.IntegerField(default=0, blank=False)

    def __unicode__(self):
        return unicode(self.user)


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length="50", blank=True, default='')
    title = models.CharField(max_length="50", blank=True, default='')
    company = models.CharField(max_length="50", blank=True, default='')
    status = models.CharField(max_length=10, choices=enum.guest_status_choices, blank=False,
                              null=False, default='UNKNOWN')

    def __unicode__(self):
        return unicode(self.user)

