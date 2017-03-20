# Django
from django.contrib import admin

# local Django
from .models import Post
from .models import UserProfile


admin.site.register(Post)
admin.site.register(UserProfile)
