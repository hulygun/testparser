# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class UrlParse(models.Model):
    STATUSES = (
        (0, 'just created'),
        (1, 'add to queue'),
        (2, 'parse success'),
        (-1, 'parse success'),
    )
    url = models.URLField()
    timeshift = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0,choices=STATUSES, editable=False)
    page_title = models.CharField(max_length=15, null=True, blank=True, editable=False)
    page_charset = models.CharField(max_length=255, null=True, blank=True, editable=False)
    page_h1_tag = models.CharField(max_length=255, null=True, blank=True, editable=False)

    def __str__(self):
        return self.url