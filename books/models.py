# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    # 书名
    book_name = models.CharField(max_length = 20 )
    # 作者
    book_author = models.CharField(max_length = 10)
    # 上传日期
    book_update = models.DateTimeField(auto_now_add = True)
    # 书籍描述
    book_description = models.CharField(max_length=255)
    # 下载量
    book_download_count = models.IntegerField()

    class Meta:
        db_table = 'books'