from django.db import models


class PSM25Question(models.Model):

    question_text = models.TextField(verbose_name='Текст вопроса', null=False, blank=False, max_length=5000)


class PSM25UserAnswer(models.Model):

    test_id = models.UUIDField(verbose_name='UUID теста', blank=False, null=False)
    answer = models.IntegerField(verbose_name='Текст ответа', null=False, default=0)
