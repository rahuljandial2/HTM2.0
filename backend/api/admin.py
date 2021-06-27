from django.contrib import admin

from .models import Profile, Task, VerifyKey

admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(VerifyKey)
