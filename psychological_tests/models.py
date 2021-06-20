from uuid import uuid4

from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import reverse


class UserExtended(AbstractUser):

    fio = models.CharField(verbose_name='ФИО', max_length=500, null=False, blank=True)
    group_code = models.CharField(verbose_name='Код группы', max_length=500, null=False, blank=True)


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

    user = models.ForeignKey(UserExtended, verbose_name='Пользователь', null=False, on_delete=models.CASCADE)
    test_type = models.PositiveBigIntegerField(verbose_name='Тип теста', blank=False, null=False, choices=TESTS)
    finished = models.BooleanField(verbose_name='Попытка завершена', default=False)
    test_uuid = models.UUIDField(verbose_name='UUID попытки теста', default=uuid4, null=False)

    def get_name(self):
        if self.test_type == self.PSM25_TEST:
            return 'ШКАЛА ПСИХОЛОГИЧЕСКОГО СТРЕССА PSM-25'
        elif self.test_type == self.TAILOR_TEST:
            return 'СКЛОННОСТЬ К РАЗВИТИЮ СТРЕССА'
        elif self.test_type == self.EMOTIONAL_BURNOUT_TEST:
            return 'ПСИХОЛОГИЧЕСКОЕ ВЫГОРАНИЕ'

    def generate_link(self):
        return reverse('test-result', kwargs={'test_uuid': self.test_uuid})

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
        elif self.test_type == self.EMOTIONAL_BURNOUT_TEST:
            return EmotionalBurnoutResult.objects.get(result_uuid=self.test_uuid)

    def finish_test(self):
        if self.test_type == self.PSM25_TEST:
            self.finish_psm25()
        elif self.test_type == self.TAILOR_TEST:
            self.finish_tailor()
        elif self.test_type == self.EMOTIONAL_BURNOUT_TEST:
            self.finish_emotional_burnout()

    def get_user_answers(self):
        return UserAnswer.objects.filter(test_attempt=self)

    def finish_psm25(self):
        user_answers = self.get_user_answers()

        score = sum(map(lambda answer: answer.answer, user_answers))
        PSM25TestResult.objects.create(score=score, result_uuid=self.test_uuid)

    tailor_score_mapping = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]

    def finish_tailor(self):
        user_answers = self.get_user_answers()

        score_sum = 0

        for answer in user_answers:
            score_marker = self.tailor_score_mapping[answer.question_number - 1]
            if score_marker == answer.answer:
                score_sum += 1

        TailorTestResult.objects.create(result_uuid=self.test_uuid, score=score_sum)

    emotional_burnout_score_mapping = [
        (1, 2, 'traumatic_circumstance'),  # 1
        (0, 3, 'self_dissatisfaction'),  # 2
        (1, 10, 'caged'),  # 3
        (1, 2, 'depression'),  # 4
        (1, 5, 'inappropriate_response'),  # 5
        (1, 10, 'emotional_disorientation'),   # 6
        (1, 2, 'emotion_economy'),  # 7
        (1, 5, 'professional_duties_reduction'),  # 8
        (1, 3, 'emotional_deficit'),  # 9
        (1, 2, 'emotional_detachment'),  # 10
        (1, 5, 'personal_detachment'),  # 11
        (1, 3, 'psychosomatic_and_psychovegetative_disorders'),  # 12
        (1, 3, 'traumatic_circumstance'),  # 13
        (1, 2, 'self_dissatisfaction'),  # 14
        (1, 5, 'caged'),  # 15
        (1, 3, 'depression'),  # 16
        (0, 3, 'inappropriate_response'),   # 17
        (0, 3, 'emotional_disorientation'),
        (1, 10, 'emotion_economy'),
        (1, 5, 'professional_duties_reduction'),
        (1, 2, 'emotional_deficit'),
        (1, 3, 'emotional_detachment'),
        (1, 3, 'personal_detachment'),
        (1, 2, 'psychosomatic_and_psychovegetative_disorders'),
        (1, 2, 'traumatic_circumstance'),  # 25
        (1, 2, 'self_dissatisfaction'),
        (1, 2, 'caged'),
        (1, 5, 'depression'),
        (1, 10, 'inappropriate_response'),
        (1, 3, 'emotional_disorientation'),
        (0, 2, 'emotion_economy'),
        (1, 2, 'professional_duties_reduction'),
        (1, 5, 'emotional_deficit'),
        (0, 2, 'emotional_detachment'),
        (1, 3, 'personal_detachment'),
        (1, 5, 'psychosomatic_and_psychovegetative_disorders'),
        (0, 3, 'traumatic_circumstance'),  # 37
        (0, 10, 'self_dissatisfaction'),  # 38
        (1, 2, 'caged'),
        (1, 5, 'depression'),
        (1, 2, 'inappropriate_response'),
        (1, 5, 'emotional_disorientation'),
        (1, 5, 'emotion_economy'),
        (0, 2, 'professional_duties_reduction'),
        (0, 5, 'emotional_deficit'),
        (1, 3, 'emotional_detachment'),
        (1, 5, 'personal_detachment'),
        (1, 3, 'psychosomatic_and_psychovegetative_disorders'),
        (1, 10, 'traumatic_circumstance'),  # 49
        (0, 5, 'self_dissatisfaction'),  # 50
        (1, 5, 'caged'),
        (1, 10, 'depression'),
        (1, 2, 'inappropriate_response'),
        (1, 2, 'emotional_disorientation'),
        (1, 3, 'emotion_economy'),
        (1, 3, 'professional_duties_reduction'),
        (1, 3, 'emotional_deficit'),
        (1, 5, 'emotional_detachment'),
        (1, 5, 'personal_detachment'),
        (1, 2, 'psychosomatic_and_psychovegetative_disorders'),
        (1, 5, 'traumatic_circumstance'),  # 61
        (1, 5, 'self_dissatisfaction'),
        (1, 1, 'caged'),
        (1, 2, 'depression'),
        (1, 3, 'inappropriate_response'),
        (1, 2, 'emotional_disorientation'),
        (1, 3, 'emotion_economy'),
        (1, 3, 'professional_duties_reduction'),
        (0, 10, 'emotional_deficit'),
        (1, 5, 'emotional_detachment'),
        (1, 2, 'personal_detachment'),
        (1, 10, 'psychosomatic_and_psychovegetative_disorders'),
        (0, 5, 'traumatic_circumstance'),  # 73
        (1, 3, 'self_dissatisfaction'),
        (0, 5, 'caged'),
        (1, 3, 'depression'),
        (1, 5, 'inappropriate_response'),
        (0, 5, 'emotional_disorientation'),
        (0, 5, 'emotion_economy'),
        (1, 10, 'professional_duties_reduction'),
        (1, 2, 'emotional_deficit'),
        (1, 10, 'emotional_detachment'),
        (1, 10, 'personal_detachment'),
        (1, 5, 'psychosomatic_and_psychovegetative_disorders'),
    ]

    def finish_emotional_burnout(self):
        user_answers = self.get_user_answers()

        result = {
            'result_uuid': self.test_uuid,
            'traumatic_circumstance': 0,
            'self_dissatisfaction': 0,
            'caged': 0,
            'depression': 0,
            'inappropriate_response': 0,
            'emotional_disorientation': 0,
            'emotion_economy': 0,
            'professional_duties_reduction': 0,
            'emotional_deficit': 0,
            'emotional_detachment': 0,
            'personal_detachment': 0,
            'psychosomatic_and_psychovegetative_disorders': 0,
        }

        for answer in user_answers:
            score_map = self.emotional_burnout_score_mapping[answer.question_number - 1]

            if score_map[0] == answer.answer:
                result[score_map[2]] = result.get(score_map[2], 0) + score_map[1]

        EmotionalBurnoutResult.objects.create(**result)

    def get_test_result(self):
        if self.test_type == self.PSM25_TEST:
            return PSM25TestResult.objects.get(result_uuid=self.test_uuid)
        elif self.test_type == self.TAILOR_TEST:
            return TailorTestResult.objects.get(result_uuid=self.test_uuid)
        elif self.test_type == self.EMOTIONAL_BURNOUT_TEST:
            return EmotionalBurnoutResult.objects.get(result_uuid=self.test_uuid)


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


class EmotionalBurnoutResult(models.Model):

    result_uuid = models.UUIDField(verbose_name='UUID результата (совпадает с UUID теста)', default=uuid4, unique=True,
                                   null=False)

    # Категория напряжение (stress)
    traumatic_circumstance = models.PositiveIntegerField(verbose_name='Переживание психотравмирующих обстоятельств',
                                                         null=False)
    self_dissatisfaction = models.PositiveIntegerField(verbose_name='Неудовлетворенность собой', null=False)
    caged = models.PositiveIntegerField(verbose_name='Загнанност в клетку', null=False)
    depression = models.PositiveIntegerField(verbose_name='Тревога и депрессия', null=False)

    # Категория резистенция (resistance)
    inappropriate_response = models.PositiveIntegerField(
        verbose_name='Неадекватное избирательное эмоциональное реагирование', null=False
    )
    emotional_disorientation = models.PositiveIntegerField(verbose_name='Эмоционально-нравственная дизориентация')
    emotion_economy = models.PositiveIntegerField(verbose_name='Расширение сферы экономии эмоций', null=False)
    professional_duties_reduction = models.PositiveIntegerField(verbose_name='Редукция сферы экономии эмоций',
                                                                null=False)

    # Категория истощение (exhaustion)
    emotional_deficit = models.PositiveIntegerField(verbose_name='Эмоциональный дефицит', null=False)
    emotional_detachment = models.PositiveIntegerField(verbose_name='Эмоциональная отстраненность',
                                                       null=False)
    personal_detachment = models.PositiveIntegerField(verbose_name='Личная отстраненность (деперсонализация)',
                                                      null=False)
    psychosomatic_and_psychovegetative_disorders = models.PositiveIntegerField(
        verbose_name='Психосоматические и психовегетативные нарушения', null=False
    )

    def get_sum_for_stress(self):
        return self.traumatic_circumstance + self.self_dissatisfaction + self.caged + self.depression

    def get_sum_for_resistance(self):
        return self.inappropriate_response + self.emotional_disorientation + self.emotion_economy + \
               self.professional_duties_reduction

    def get_sum_for_exhaustion(self):
        return self.emotional_deficit + self.emotional_detachment + self.personal_detachment + \
               self.psychosomatic_and_psychovegetative_disorders

    def get_stage_status(self, score):
        if score <= 36:
            return 'Стадия не сформировалась.'
        elif score <= 60:
            return 'В стадии формирования.'
        else:
            return 'Стадия сформировалась.'

    def get_message_for_stress(self):
        return self.get_stage_status(self.get_sum_for_stress())

    def get_message_for_resistance(self):
        return self.get_stage_status(self.get_sum_for_resistance())

    def get_message_for_exhaustion(self):
        return self.get_stage_status(self.get_sum_for_exhaustion())

    def get_symptom_status(self, score):
        if score < 10:
            return 'Симптом не сложился'
        elif score < 16:
            return 'Складывающийся симптом'
        elif score < 20:
            return 'Симптом сложился'
        else:
            return 'Симптом сложился. Доминирующий симптом.'

    def get_message_for_traumatic_circumstance(self):
        return self.get_symptom_status(self.traumatic_circumstance)

    def get_message_for_self_dissatisfaction(self):
        return self.get_symptom_status(self.self_dissatisfaction)

    def get_message_for_depression(self):
        return self.get_symptom_status(self.depression)

    def get_message_for_caged(self):
        return self.get_symptom_status(self.caged)

    def get_message_for_inappropriate_response(self):
        return self.get_symptom_status(self.inappropriate_response)

    def get_message_for_emotional_disorientation(self):
        return self.get_symptom_status(self.emotional_disorientation)

    def get_message_for_emotion_economy(self):
        return self.get_symptom_status(self.emotion_economy)

    def get_message_for_professional_duties_reduction(self):
        return self.get_symptom_status(self.professional_duties_reduction)

    def get_message_for_emotional_deficit(self):
        return self.get_symptom_status(self.emotional_deficit)

    def get_message_for_emotional_detachment(self):
        return self.get_symptom_status(self.emotional_detachment)

    def get_message_for_personal_detachment(self):
        return self.get_symptom_status(self.personal_detachment)

    def get_message_for_psychosomatic_and_psychovegetative_disorders(self):
        return self.get_symptom_status(self.psychosomatic_and_psychovegetative_disorders)
