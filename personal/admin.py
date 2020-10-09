from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin

from .models import UserProfile, Work, Project, Intro, Blog


class MyModelAdmin(MCEFilebrowserAdmin):
    pass


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Work)
admin.site.register(Project)
admin.site.register(Intro)
admin.site.register(Blog)
# admin.site.register(MCEFilebrowserAdmin)
