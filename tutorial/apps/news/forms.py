from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Article

class ArticleForm(ModelForm):
  class Meta:
    model = Article

    fields = ('headline', 'content', 'reporter', 'pub_date')
    labels = {
      'pub_date': _('Publish Date'),
      'reporter': _('Reporter Name')
    }
