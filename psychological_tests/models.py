from uuid import uuid4

from django.db import models

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


class BasicQuestion(models.Model):
    question_text = models.TextField(verbose_name='Текст вопроса', null=False, blank=False, max_length=5000)

    class Meta:
        abstract = True


class PSM25Question(BasicQuestion):
    pass


class TailorQuestion(BasicQuestion):
    pass


class EmotionalBurnoutQuestion(BasicQuestion):
    pass


class UserTest(models.Model):

    PSM25_TEST = 0
    TAILOR_TEST = 1
    EMOTIONAL_BURNOUT_TEST = 2

    TESTS = (
        (PSM25_TEST, 'PSM25 test'),
        (TAILOR_TEST, 'Tailor test'),
        (EMOTIONAL_BURNOUT_TEST, 'Emotional Burnout test')
    )

    user = models.ForeignKey(User, verbose_name='Пользователь', null=False, on_delete=models.CASCADE)
    test_type = models.PositiveBigIntegerField(verbose_name='Тип теста', blank=False, null=False, choices=TESTS)
    finished = models.BooleanField(verbose_name='Попытка завершена', default=False)
    test_uuid = models.UUIDField(verbose_name='UUID попытки теста', default=uuid4, null=False)

    def get_question_by_type(self):
        if self.test_type == self.PSM25_TEST:
            return PSM25Question.objects.all()
        elif self.test_type == self.TAILOR_TEST:
            return TailorQuestion.objects.all()
        elif self.test_type == self.EMOTIONAL_BURNOUT_TEST:
            return EmotionalBurnoutQuestion.objects.all()

    def get_result_by_type(self):
        if not self.finished:
            return None
        if self.test_type == self.PSM25_TEST:
            return PSM25TestResult.objects.get(result_uuid=self.test_uuid)
        elif self.test_type == self.TAILOR_TEST:
            return TailorTestResult.objects.get(result_uuid=self.test_uuid)

    def finish_test(self):
        if self.test_type == self.PSM25_TEST:
            self.finish_psm25()
        elif self.test_type == self.TAILOR_TEST:
            self.finish_tailor()
        elif self.test_type == self.EMOTIONAL_BURNOUT_TEST:
            return EmotionalBurnoutQuestion.objects.all()

    def get_user_answers(self):
        return UserAnswer.objects.filter(test_attempt=self)

    def finish_psm25(self):
        user_answers = self.get_user_answers()

        score = sum(map(lambda answer: answer.answer, user_answers))
        PSM25TestResult.objects.create(score=score, result_uuid=self.test_uuid)

    scored_answer_for_tailor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]

    def finish_tailor(self):
        user_answers = self.get_user_answers()

        score_sum = 0

        for answer in user_answers:
            score_marker = self.scored_answer_for_tailor[answer.question_number - 1]
            if score_marker == answer.answer:
                score_sum += 1

        TailorTestResult.objects.create(result_uuid=self.test_uuid, score=score_sum)

    def get_test_result(self):
        if self.test_type == self.PSM25_TEST:
            return PSM25TestResult.objects.get(result_uuid=self.test_uuid)
        elif self.test_type == self.TAILOR_TEST:
            return TailorTestResult.objects.get(result_uuid=self.test_uuid)
        elif self.test_type == self.EMOTIONAL_BURNOUT_TEST:
            return EmotionalBurnoutQuestion.objects.all()


class UserAnswer(models.Model):
    test_attempt = models.ForeignKey(UserTest, verbose_name='Запись теста', null=False, on_delete=models.CASCADE)
    answer = models.IntegerField(verbose_name='Текст ответа', null=False, default=0)
    question_number = models.PositiveIntegerField(verbose_name='Номер вопроса', null=False)


class PSM25TestResult(models.Model):

    score = models.PositiveIntegerField(verbose_name='', null=False, blank=False)
    result_uuid = models.UUIDField(verbose_name='UUID результата (совпадает с UUID теста)', default=uuid4, unique=True,
                                   null=False)


class TailorTestResult(models.Model):

    score = models.PositiveIntegerField(verbose_name='', null=False, blank=False)
    result_uuid = models.UUIDField(verbose_name='UUID результата (совпадает с UUID теста)', default=uuid4, unique=True,
                                   null=False)
