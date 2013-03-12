# -*- coding:utf8 -*-

from django.db import models
from taxonomy.models import Genre, Country, Language
from people.models import Celebrity


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, verbose_name=u"类型")
    countries = models.ManyToManyField(Country, verbose_name=u"国家/地区")
    languages = models.ManyToManyField(Language, verbose_name=u"语言")

    directors = models.ManyToManyField(Celebrity, related_name="direct_movies", verbose_name=u"导演", null=True, blank=True)
    writers = models.ManyToManyField(Celebrity, related_name="write_movies", verbose_name=u"编剧", null=True, blank=True)
    actors = models.ManyToManyField(Celebrity, related_name="act_movies", verbose_name=u"主演", null=True, blank=True)

    name = models.CharField(u"片名", max_length=50)
    poster = models.ImageField(u"海报", upload_to='poster', null=True, blank=True)
    year = models.IntegerField(u"年份", max_length=4)
    length = models.IntegerField(u"片长")

    imdb = models.CharField(u"imdb编号", max_length=50, null=True, blank=True)
    website = models.URLField(u"官网", null=True, blank=True)
    release_time = models.CharField(u"上映/首播日期", max_length=50, null=True, blank=True)
    play_urls = models.TextField(u"播放列表", null=True, blank=True)
    intro = models.TextField(u"剧情", null=True, blank=True)


    # 电视剧特有
    is_tv = models.BooleanField(u"电视剧", default=False)
    tv_station = models.CharField(u"电视台", max_length=50, null=True, blank=True)
    quarter = models.IntegerField(u"季", null=True, blank=True)
    episodes = models.IntegerField(u"集数", null=True, blank=True)

    seo = models.TextField(u"SEO优化", null=True, blank=True)

    is_publish = models.BooleanField(u"发布", default=True)
    date_created = models.DateTimeField(u"添加日期", auto_now_add=True)
    date_modified = models.DateTimeField(u"最后修改", auto_now=True)

    class Meta:
        verbose_name = u"影片"
        verbose_name_plural = verbose_name
        get_latest_by = "date_modified"

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.year)


class MovieAlias(models.Model):
    movie = models.ForeignKey(Movie, verbose_name=u"原影片", related_name='alias')
    alias_name = models.CharField(u"别名", max_length=50)

    class Meta:
        verbose_name = u"影片别名"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.alias_name
