# -*- coding:utf8 -*-

from django.contrib import admin
from stats.models import *


class HintAdmin(admin.ModelAdmin):
    list_display = ('movie', 'hints_day', 'hints_week', 'hints_month', 'hints_total', )

admin.site.register(Hint, HintAdmin)