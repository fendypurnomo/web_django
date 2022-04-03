from django.contrib import admin
from .forms import ArticleForm
from .models import Article, Reporter

@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_filter = ['full_name']
    search_fields = ['full_name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ['headline', 'reporter', 'pub_date']
    list_filter = ['headline', 'reporter', 'pub_date']
    search_fields = ['headline', 'reporter__full_name', 'pub_date']
