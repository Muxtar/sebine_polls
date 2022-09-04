from django.contrib import admin
from polls.models import Polls, Questions, Answers

# Register your models here.


@admin.register(Polls)
class PollsAdmin(admin.ModelAdmin):
    fields = ('name', 'minute', 'count', 'percent')


class AnswersAdmin(admin.TabularInline):
    model = Answers
    fields = ('questions', 'answer', 'rightAnswer')

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    fields = ('polls', 'question')
    inlines = [AnswersAdmin]