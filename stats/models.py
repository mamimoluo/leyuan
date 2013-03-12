# -*- coding:utf8 -*-

from django.db import models
from film.models import Movie


# 点击统计
class Hint(models.Model):
    u"""用于统计电影的日点击、周点击、月点击、总点击数
    """
    movie = models.OneToOneField(Movie, verbose_name=u"影片")
    hints_day = models.IntegerField(u"日点击数", default=100)
    hints_week = models.IntegerField(u"周点击数", default=100)
    hints_month = models.IntegerField(u"月点击数", default=100)
    hints_total = models.IntegerField(u"总点击数", default=100)

    class Meta:
        verbose_name = u"点击统计"
        verbose_name_plural = verbose_name
