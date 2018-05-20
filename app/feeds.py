# -*- encoding: utf-8 -*-

from django.contrib.syndication.views import Feed
from .models import Article


class AllArticleRssFeed(Feed):
    title = '个人博客'
    link = '/'

    # 需要显示的条目
    def items(self):
        return Article.objects.all()[:5]

    # 显示内容的标题
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    # rss中显示的描述
    def item_description(self, item):
        return item.body[:20]
