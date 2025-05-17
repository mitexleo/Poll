from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Number of empty choice fields to display

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')  # Optional: improves admin list view

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)  # Optional: keeps Ch