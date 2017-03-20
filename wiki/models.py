# future
from __future__ import unicode_literals

# Django
from django.db import models
from django.contrib.auth.models import User


USER_LEVEL = [(i,i) for i in range(0, 6)]


class UserProfile(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, related_name='user_name'
    )
    username = models.CharField(
        max_length=15, unique=True, null=False, blank=False
    )
    fullName = models.CharField(max_length=45)
    email = models.CharField(max_length=75)
    userLevel = models.IntegerField(choices=USER_LEVEL, default=0)
    lastUpdatedBy = models.ForeignKey(
        User, null=True, blank=True, default=user
    )
    lastUpdated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.fullName


class Post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=120, unique=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    lastUpdated = models.DateTimeField(auto_now=True, auto_now_add=False)
    viewPermissionLevel = models.IntegerField(
        choices=USER_LEVEL, default=0
    )
    editPermissionLevel = models.IntegerField(
        choices=USER_LEVEL, default=0
    )

    def __unicode__(self):
        return self.title
