from django.contrib import admin
from . import models

@admin.register(models.GroupGenre)
class GroupGenreAdmin(admin.ModelAdmin):
  list_display = ('name',)
  list_per_page = 10
  search_fields = ('name',)

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
  list_display = ('name', 'group_genre')
  list_filter = ('group_genre__name',)
  list_per_page = 10
  search_fields = ('name', 'group_genre__name')

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
  fields = ('first_name', 'middle_name', 'last_name', ('date_of_birth', 'date_of_death'), 'description', 'photo_profile')
  list_display = ('display_fullname', 'date_of_birth', 'date_of_death')
  list_per_page = 10
  search_fields = ('first_name', 'middle_name', 'last_name')

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
  list_display = ('name',)
  list_per_page = 10
  search_fields = ('name',)

class BookInstanceInline(admin.TabularInline):
  model = models.BookInstance

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
  inlines = [BookInstanceInline]
  fields = ('title', 'summary', 'author', 'genre', 'language', 'isbn10', 'isbn13', 'cover')
  list_display = ('title', 'display_author', 'display_genre')
  list_per_page = 10
  search_fields = ('title',)

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {
      'fields': ('book', 'imprint', 'id')
    }),
    ('Availability',
      {'fields': ('status', 'due_back')
    })
  )
  list_display = ('book', 'status', 'borrower', 'due_back', 'id')
  list_filter = ('status', 'due_back')
  list_per_page = 10
  search_fields = ('book', 'status')
