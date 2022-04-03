from django.contrib import admin
from .forms import ChoiceForm, QuestionForm
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    form = ChoiceForm
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    inlines = [ChoiceInline]
    fieldsets = (
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    )
    list_filter = ('pub_date',)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ('question_text', 'pub_date')
