from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from . import models, serializers

def all_article(request):
    list = models.Article.objects.all()
    context = {'title': 'All News', 'heading': 'All News', 'article_list': list}
    return render(request, 'apps/news/all_article.html', context)

def year_article(request, year):
    list = models.Article.objects.filter(pub_date__year=year)
    context = {'title': 'All News', 'heading': 'All News', 'year': year, 'article_list': list}
    return render(request, 'apps/news/all_article.html', context)

def month_article(request, year, month):
    list = models.Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'title': 'All News', 'heading': 'All News', 'year': year, 'month': month, 'article_list': list}
    return render(request, 'apps/news/all_article.html', context)

def	article_detail(request, year, month, pk):
    list = get_object_or_404(models.Article, pub_date__year=year, pub_date__month=month, id=pk)
    context = {'title': 'News', 'heading': 'News', 'year': year, 'month': month, 'id': pk, 'article': list}
    return render(request, 'apps/news/article_detail.html', context)

class ReporterViewSet(viewsets.ModelViewSet):
    queryset = models.Reporter.objects.all().order_by('id')
    serializer_class = serializers.ReporterSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all().order_by('-pub_date')
    serializer_class = serializers.ArticleSerializer
