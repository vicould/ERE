# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return '/~ere/authors/%s' % self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/~ere/tags/%s' % self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/~ere/categories/%s' % self.name


class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    extract = models.TextField()
    category = models.ForeignKey(Category)
    allow_comments = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/~ere/pages/%s" % self.title


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    date = models.DateTimeField()
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category)
    content = models.TextField()
    extract = models.TextField()
    allow_comments = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/~ere/%s/%s/%s" % (self.date.year, self.date.strftime("%m"), self.id)


class TopMenuElement(models.Model):
    element = models.CharField(max_length=20)
    url_suffix = models.CharField(max_length=100, blank=True) # blank is for home
    position = models.IntegerField()

    def __unicode__(self):
        return self.element

    def get_absolute_url(self):
        return '/~ere/%s' % self.url_suffix


class LeftMenuElement(models.Model):
    element = models.CharField(max_length=20)
    url_suffix = models.CharField(max_length=100, blank=True)
    position = models.IntegerField()

    def __unicode__(self):
        return self.element

    def get_absolute_url(self):
        return '/~ere/%s' % self.url_suffix


class Meeting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    category = models.ForeignKey(Category)
    description = models.OneToOneField(Article, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/~ere/meetings/%s/%s/%s/%s' % (self.date.year,
                                       self.date.month,
                                       self.date.day,
                                       self.id)

