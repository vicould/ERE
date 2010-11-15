from django.contrib.syndication.views import Feed
from  blog.models import Article

class RecentArticlesFeed(Feed):
    title = "Les derniers articles du site de l'ERE"
    link = "/"
    description = "Flux regroupant les derniers articles du site de l'ERE"

    def items(self):
        return Article.objects.order_by('-date')[:5]

    def items_title(self, item):
        return item.title

    def item_description(self, item):
        return item.extract
