# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . models import *

class AdminUserProfile(admin.ModelAdmin):
	lsit_display = ['firstname','lastname','phone','sex']


admin.site.register(UserProfile,AdminUserProfile)