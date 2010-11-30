from django.conf.urls.defaults import *
from django.views.generic import date_based
from ere.blog.models import Article
from ere.blog.feeds import RecentArticlesFeed

year_re = '(?P<year>\d{4})'
month_re = '(?P<month>\d{2})'
day_re = '(?P<day>\d{2})'
article_id_re = '(?P<article_id>\d+)'
tag_string = 'tags'
tag_re = '(?P<tag_name>\w+)'
authors_string = 'authors'
author_re = '(?P<author>\w+)'
pages_string = 'pages'
page_re = '(?P<page_title>.+)'
category_string = 'categories'
category_re = '(?P<category_name>.+)'
date_string = 'meetings'
meeting_id_re = '(?P<meeting_id>\d+)'

article_query_basis_dictionary = { 'queryset' : Article.objects.all(), 'date_field' :
                     'date'}

urlpatterns = patterns('ere.blog.views',
    (r'^$',
     date_based.archive_index,
     dict(article_query_basis_dictionary.items() + { 'template_object_name' :
                                            'object_list' }.items())),
    (r'^%(year_re)s/$' % locals(),
     date_based.archive_year,
     dict(article_query_basis_dictionary.items() + { 'make_object_list' : True }.items())),
    (r'^%(year_re)s/%(month_re)s/$' % locals(),
     date_based.archive_month,
     dict(article_query_basis_dictionary.items() + { 'month_format' : '%m' }.items())),
    (r'^%(year_re)s/%(month_re)s/%(article_id_re)s/$' % locals(), 'article_entry'),
    (r'^%(tag_string)s/$' % locals(), 'tag_cloud'),
    (r'^%(tag_string)s/%(tag_re)s/$' % locals(), 'tag_cloud_result'),
    (r'^%(authors_string)s/$' % locals(), 'author_list'),
    (r'^%(authors_string)s/%(author_re)s/$' % locals(), 'author'),
    (r'^latest/feed/$', RecentArticlesFeed()),
    (r'^%(pages_string)s/$' % locals(), 'pages_index' ),
    (r'^%(pages_string)s/%(page_re)s/$' % locals(), 'page_entry' ),
    (r'^%(category_string)s/$' % locals(), 'categories_index'),
    (r'^%(category_string)s/%(category_re)s/$' % locals(), 'category_detail'),
    (r'^%(date_string)s/$' % locals(), 'meetings_index'),
    (r'^%(date_string)s/%(year_re)s/%(month_re)s/%(day_re)s/%(meeting_id_re)s/$' % locals(),
     'meeting_detail'),
)
