from django.contrib import admin
from django.utils import timezone

from datetime import timedelta

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information',{'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'is_recent')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    @admin.display(boolean=True, ordering='pub_date', description='Published recently?')
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now

admin.site.register(Question, QuestionAdmin)
