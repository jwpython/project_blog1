from django.contrib import admin

# Register your models here.

from blog_app.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    # class Media:
    #     js = (
    #         '/static/js/tinymce/tinymce.mce.js',
    #         '/static/js/textareas.js',
    #  )


admin.site.register(Article, ArticleAdmin)
