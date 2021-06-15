from django.db import models


class PSM25Question(models.Model):

    question_text = models.TextField(verbose_name='Текст вопроса', null=False, blank=False, max_length=5000)
