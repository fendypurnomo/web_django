from rest_framework import serializers
from .models import Reporter, Article

class	ReporterSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Reporter

    fields = ('id', 'full_name')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
  reporter = serializers.StringRelatedField()

  class Meta:
    model = Article

    fields = ('id', 'pub_date', 'reporter', 'headline', 'content')
