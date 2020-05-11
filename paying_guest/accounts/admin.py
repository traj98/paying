# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . models import *

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('firstname','lastname','phone','sex')
	search_fields =('firstname','lastname')
	
	list_per_page = 25


admin.site.register(UserProfile,ProfileAdmin)