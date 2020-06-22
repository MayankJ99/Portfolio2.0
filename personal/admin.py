from django.contrib import admin
from .models import UserProfile, Work, Project, Intro
from . import models


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Work)
admin.site.register(Project)
admin.site.register(Intro)



