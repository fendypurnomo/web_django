from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
  path('', views.all_article, name='all_article'),
  path('<int:year>/', views.year_article, name='year_article'),
  path('<int:year>/<int:month>/', views.month_article, name='month_article'),
  path('<int:year>/<int:month>/<int:pk>/', views.article_detail, name='article_detail')
]
