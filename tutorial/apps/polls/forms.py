from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Choice, Question

class QuestionForm(ModelForm):
  class Meta:
    model = Question
    fields = ('question_text', 'pub_date')
    labels = {'question_text': _('Question')}

class ChoiceForm(ModelForm):
  class Meta:
    model = Choice
    fields = ('choice_text', 'votes')
    labels = {'choice_text': _('Choice')}
