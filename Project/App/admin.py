from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, AdminVideo)
admin.site.register((Userinfo,Visitor))
