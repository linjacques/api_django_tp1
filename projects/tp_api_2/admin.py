from django.contrib import admin
from .models.user import User
from .models.log import ResourceLog

admin.site.register(User)
admin.site.register(ResourceLog)