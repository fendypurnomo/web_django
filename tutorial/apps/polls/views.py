from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
  template_name = 'apps/polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
  model = Question
  template_name = 'apps/polls/detail.html'

  def get_queryset(self):
    return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'apps/polls/results.html'

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)

  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    context = {
      'question': question,
      'error_message': "You didn't select a choice."
    }
    return render(request, 'apps/polls/detail.html', context)
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
