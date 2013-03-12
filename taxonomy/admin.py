# -*- coding:utf8 -*-

from django.contrib import admin
from taxonomy.models import *

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Profession)