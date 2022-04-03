import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from datetime import date

class GroupGenre(models.Model):
    name = CharField(max_length=75, verbose_name='Group Genre Name')

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Sciene Fiction)', verbose_name='Genre Name')
    group_genre = models.ForeignKey(GroupGenre, on_delete=models.SET_NULL, null=True, verbose_name='Genre Group')

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField('died', blank=True, null=True)
    description = models.TextField(max_length=1500, blank=True, null=True)
    photo_profile = models.ImageField(upload_to='catalog/authors/', blank=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self) -> str:
        if (self.middle_name): middle_name = self.middle_name
        else: middle_name = ''

        if (self.last_name): last_name = self.last_name
        else: last_name = ''

        return f'{self.first_name} {middle_name} {last_name}'

    def get_absolute_url(self):
        return reverse('catalog:author-detail', args=[str(self.id)])

    def display_fullname(self):
        if (self.middle_name): middle_name = self.middle_name
        else: middle_name = ''

        if (self.last_name): last_name = self.last_name
        else: last_name = ''

        return f'{self.first_name} {middle_name} {last_name}'

    display_fullname.short_description = 'Fullname'

class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", verbose_name='Language Name')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1500, help_text='Enter a brief description of the book')
    isbn10 = models.CharField('ISBN 10', max_length=10, unique=True, blank=True, null=True, help_text='10 Character <a href="https://www.isbn-internasional.org/content/what-isbn">ISBN number</a>')
    isbn13 = models.CharField('ISBN 13', max_length=13, unique=True, blank=True, null=True, help_text='13 Character <a href="https://www.isbn-internasional.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    author = models.ManyToManyField(Author, help_text='Select an author for this book')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    cover = models.ImageField(upload_to='catalog/books/', blank=True, null=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:book-detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()[:3]])

    display_author.short_description = 'Author'

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='m', blank=True, help_text='Book availability')

    class Meta:
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self) -> str:
        return f'{self.id} ({self.book.title})'
