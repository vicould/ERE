# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from ere.blog.models import Article, Tag, Author, Category, Page, Meeting


def index(request):
    latest_entries_list = Article.objects.all().order_by('-date')[:5]
    return render_to_response('blog/index.html', {'latest_entries_list': latest_entries_list,})


def year_archive(request, year):
    year_archive_list = Article.objects.filter(date__year=year).order_by('-date')
    return render_to_response('blog/yearly_archives.html', {'year_archive_list': year_archive_list,})


def month_archive(request, year, month):
    month_archive_list = Article.objects.filter(date__year=year, date__month=month)
    return render_to_response('blog/monthly_archives.html', {'month_archive_list': month_archive_list,})


def article_entry(request, year, month, article_id):
    a = get_object_or_404(Article, date__year=year, date__month=month, id=article_id,)
    return render_to_response('blog/article_entry.html', {'article_entry': a}, context_instance=RequestContext(request))


def tag_cloud(request):
    tag_list = Tag.objects.all()
    tag_dict = {}
    total_tagged = 0

    for tag_item in tag_list:
        length = Article.objects.filter(tag__name__exact=tag_item).count()
        tag_dict = dict(tag_dict.items() + 
                              { tag_item : length }.items())
        total_tagged += length

    for tag_entry in tag_dict.iterkeys():
        tag_dict[tag_entry] = tag_dict[tag_entry]/float(total_tagged)
    
    return render_to_response('blog/tag_cloud.html', {'tag_dict': tag_dict}, context_instance=RequestContext(request))


def tag_cloud_result(request, tag_name):
    tagged_articles_list = Article.objects.filter(tag__name=tag_name)
    return render_to_response('blog/tag_cloud_results.html', {'object_list': tagged_articles_list}, context_instance=RequestContext(request))


def author_list(request):
	author_list = Author.objects.all()
	return render_to_response('blog/alls_author.html', {'author_list': author_list}, context_instance=RequestContext(request))


def author(request, author):
	publications_list = Article.objects.filter(author__user__username=author)
	return render_to_response('blog/author_articles.html', {'object_list': publications_list}, context_instance=RequestContext(request))


def pages_index(request):
    pages_list = Page.objects.all()
    return render_to_response('blog/pages_index.html', {'pages_list' :
                                                        pages_list}, context_instance=RequestContext(request))


def page_entry(request, page_title):
    p = get_object_or_404(Page, title=page_title) 
    return render_to_response('blog/page_entry.html', {'page_entry' : p}, context_instance=RequestContext(request))


def categories_index(request):
    categories_list = Category.objects.all()
    return render_to_response('blog/categories_index.html', 
                              {'categories_list' : categories_list}, context_instance=RequestContext(request))


def category_detail(request, category_name):
    related_articles_list = \
        Article.objects.filter(category__name=category_name).order_by('date')
    related_pages_list = \
        Page.objects.filter(category__name=category_name).order_by('title')
    related_meetings_list = \
        Meeting.objects.filter(category__name=category_name).order_by('date')
    return render_to_response('blog/category_detail.html',
                              {'related_articles_list' : related_articles_list,
                               'related_pages_list' : related_pages_list,
                               'related_meetings_list' : related_meetings_list},
                              context_instance=RequestContext(request))


def meetings_index(request):
    meetings_list = Meeting.objects.all()
    return render_to_response('blog/meetings_index.html', 
                              {'meetings_list' : meetings_list},
                             context_instance=RequestContext(request))

