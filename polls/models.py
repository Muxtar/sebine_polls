from django.db import models


class ABS(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Polls(ABS):
    name = models.CharField(max_length=20)
    # keçmə vaxtı - dəqiqələrlə.
    minute = models.IntegerField()
    # kecmek cehdlerinin minumum sayi
    count = models.IntegerField()
    # Keçmək üçün düzgün cavabların minimum faizi.
    percent = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Questions(ABS):
    question = models.TextField()
    polls = models.ForeignKey(Polls, related_name='questions', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.question

class Answers(ABS):
    answer = models.TextField()
    rightAnswer = models.BooleanField()
    questions = models.ForeignKey(Questions, related_name='answers', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.answer
