# -*- coding:utf8 -*-

from django.contrib import admin
from people.models import Celebrity, CelebrityAlias


class CelebrityAliasInline(admin.StackedInline):
    model = CelebrityAlias
    extra = 1


class CelebrityAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'birthday', 'birthplace', )
    #fields = ('name', ('is_actor', 'is_director', 'is_writer', ))
    list_filter = ('sex', 'birthday', )
    date_hierarchy = 'birthday'

    inlines = [CelebrityAliasInline]

admin.site.register(Celebrity, CelebrityAdmin)


class CelebrityAliasAdmin(admin.ModelAdmin):
    list_display = ('movie', 'alias_name')

admin.site.register(CelebrityAlias, CelebrityAliasAdmin)