# -*- coding:utf8 -*-

from django.contrib import admin
from film.models import Movie, MovieAlias
from stats.models import Hint


class HintInline(admin.TabularInline):
    model = Hint


class MovieAliasInline(admin.StackedInline):
    model = MovieAlias
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'poster', 'is_publish', )
    list_filter = ('is_publish', 'genres', 'countries', 'languages', 'year', )
    search_fields = ('name', 'intro')
    ordering = ['-date_created']
    date_hierarchy = 'date_created'
    fieldsets = (
        (None, {
            'fields': (
                'genres', 'countries', 'languages',
                'directors', 'writers', 'actors',
                'name', 'poster', 'year', 'length', 'imdb', 'website', 'release_time','intro', 'play_urls',
            )
        }),
        (u"电视剧", {
            'classes': ('collapse', ),
            'fields': ('is_tv', 'tv_station', 'quarter', 'episodes', )
        }),
        (None, {
            'fields': ('seo', 'is_publish', )
        }),
    )
    inlines = [MovieAliasInline, HintInline]

admin.site.register(Movie, MovieAdmin)


class MovieAliasAdmin(admin.ModelAdmin):
    list_display = ('movie', 'alias_name')

admin.site.register(MovieAlias, MovieAliasAdmin)