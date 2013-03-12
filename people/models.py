# -*- coding:utf8 -*-

from django.db import models
from taxonomy.models import Country, Profession


class People(models.Model):
    MALE = True
    FEMALE = False
    UNKNOWN = None
    SEX_CHOICES = (
        (MALE, u"男"),
        (FEMALE, u"女"),
        (UNKNOWN, u"未知"),
    )

    name = models.CharField(u"原名", max_length=50, unique=True)
    birthday = models.DateField(u"生日", null=True, blank=True)
    birthplace = models.ForeignKey(Country, verbose_name=u"出生地", null=True, blank=True)
    profession = models.ManyToManyField(Profession, verbose_name=u"职业", null=True, blank=True)
    sex = models.NullBooleanField(u"性别", choices=SEX_CHOICES, default=UNKNOWN)
    intro = models.TextField(u"影人简介", null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Celebrity(People):
    imdb = models.CharField(u"imdb编号", max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = u"影人"
        verbose_name_plural = verbose_name


class CelebrityAlias(models.Model):
    movie = models.ForeignKey(Celebrity, verbose_name=u"原名", related_name='alias')
    alias_name = models.CharField(u"别名", max_length=50)

    class Meta:
        verbose_name = u"影人别名"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.alias_name