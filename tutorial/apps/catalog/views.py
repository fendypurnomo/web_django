import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models
from . import forms

def index(request):
  num_books = models.Book.objects.all().count()
  num_instance = models.BookInstance.objects.all().count()
  num_instances_available = models.BookInstance.objects.filter(status__exact='a').count()
  num_authors = models.Author.objects.count()
  num_visits = request.session.get('num_visits', 1)
  request.session['num_visits'] = num_visits + 1
  context = {
    'num_books': num_books,
    'num_instance': num_instance,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'num_visits': num_visits
  }
  return render(request, 'apps/catalog/index.html', context)

class BookListView(generic.ListView):
  model = models.Book
  paginate_by = 10
  template_name = 'apps/catalog/book_list.html'

class BookDetailView(generic.DetailView):
  model = models.Book
  template_name = 'apps/catalog/book_detail.html'

class AuthorListView(generic.ListView):
  model = models.Author
  paginate_by = 10
  template_name = 'apps/catalog/author_list.html'

class AuthorDetailView(generic.DetailView):
  model = models.Author
  template_name = 'apps/catalog/author_detail.html'

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
  model = models.BookInstance
  template_name = 'apps/catalog/bookinstance_list_borrowed_user.html'
  paginate_by = 10

  def get_queryset(self):
    return models.BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
  model = models.BookInstance
  permission_required = 'catalog.can_mark_returned'
  template_name = 'apps/catalog/bookinstance_list_borrowed_all.html'
  paginate_by = 10

  def get_queryset(self):
    return models.BookInstance.objects.filter(status__exact='o').order_by('due_back')

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
  book_instance = get_object_or_404(models.BookInstance, id=pk)

  if request.method == 'POST':
    form = forms.RenewBookForm(request.POST)
    if form.is_valid():
      book_instance.due_back = form.cleaned_data['renewal_date']
      book_instance.save()
      return HttpResponseRedirect(reverse('all-borrowed-books'))
  else:
    proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
    form = forms.RenewBookForm(initial={'renewal_date': proposed_renewal_date})

  context = {
    'form': form,
    'book_instance': book_instance,
  }

  return render(request, 'apps/catalog/book_renew_librarian.html', context)

class AuthorCreate(PermissionRequiredMixin, CreateView):
  model = models.Author
  fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'description', 'photo_profile']
  initial = {'date_of_death': '11/06/2020'}
  permission_required = 'catalog.can_mark_returned'
  template_name = 'apps/catalog/author_form.html'

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
  model = models.Author
  fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'description', 'photo_profile']
  permission_required = 'catalog.can_mark_returned'
  template_name = 'apps/catalog/author_form.html'

class AuthorDelete(PermissionRequiredMixin, DeleteView):
  model = models.Author
  permission_required = 'catalog.can_mark_returned'
  success_url = reverse_lazy('authors')

class BookCreate(PermissionRequiredMixin, CreateView):
  model = models.Book
  fields = ['title', 'author', 'summary', 'isbn10', 'isbn13', 'genre', 'language']
  permission_required = 'catalog.can_mark_returned'
  template_name = 'apps/catalog/book_form.html'

class BookUpdate(PermissionRequiredMixin, UpdateView):
  model = models.Book
  fields = ['title', 'author', 'summary', 'isbn10', 'isbn13', 'genre', 'language']
  permission_required = 'catalog.can_mark_returned'
  template_name = 'apps/catalog/book_form.html'

class BookDelete(PermissionRequiredMixin, DeleteView):
  model = models.Book
  permission_required = 'catalog.can_mark_returned'
  success_url = reverse_lazy('books')
