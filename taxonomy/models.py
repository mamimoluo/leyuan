# -*- coding:utf8 -*-

from django.db import models


class Taxonomy(models.Model):
    name = models.CharField(u"名称", max_length=50, unique=True)
    parent = models.ForeignKey('self', verbose_name=u"父类", null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Genre(Taxonomy):
    class Meta:
        verbose_name = u"影片类型"
        verbose_name_plural = verbose_name


class Language(Taxonomy):
    class Meta:
        verbose_name = u"语言"
        verbose_name_plural = verbose_name


class Country(Taxonomy):
    class Meta:
        verbose_name = u"国家/地区"
        verbose_name_plural = verbose_name


class Profession(Taxonomy):
    class Meta:
        verbose_name = u"职业"
        verbose_name_plural = verbose_name
