from blog.models import Article, Author, Tag, User, Category, Page
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Content', {'fields' : ['title', 'content', 'author', 'date',
                                     'extract', 'allow_comments']}),
            ('Classification', {'fields' : ['category', 'tag']})
            ]
    list_display = ('date', 'title', 'author')
    list_filter = ['date']
    search_fields = ['title']
    date_hierarchy = 'date'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Page)
