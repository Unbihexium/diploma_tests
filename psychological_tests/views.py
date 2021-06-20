from django.shortcuts import render, reverse
from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login



from psychological_tests.forms import LoginForm

from psychological_tests.models import TailorQuestion, PSM25Question, UserAnswer, UserTest, EmotionalBurnoutResult, \
    EmotionalBurnoutQuestion, UserExtended


@login_required
def main(request, *args, **kwargs):
    request.session['test_id'] = None
    return render(request, 'base.html')


def authorization(request):
    """
    Авторизация
    """
    if request.method == 'GET':
        return render(request, 'login.html')
    data = {
        'username': request.POST.get('username', '').strip(),
        'password': request.POST.get('password', ''),
    }
    login_form = LoginForm(data)
    try:
        response = login_form.is_valid()
        if response:
            user = UserExtended.objects.get(username=data['username'])
            login(request, user)
            return JsonResponse({'status': 'success'}, safe=False)
        else:
            return JsonResponse({'status': 'error'}, safe=False)
    except Exception as e:
        return JsonResponse({'status': ['Введён некорректный username или пароль, попробуйте ввести их ещё раз!']},
                            safe=False)


@method_decorator(login_required, name='dispatch')
class BaseSessionView(TemplateView):

    def dispatch(self, *args, **kwargs):
        # self.request.COOKIES['test_id'] = str(uuid4())
        return super().dispatch(*args, **kwargs)


# region psm
class PSM25TestView(BaseSessionView):
    template_name = 'psm/psm25.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_test = UserTest.objects.create(test_type=UserTest.PSM25_TEST, user=self.request.user)

        self.request.session['test_id'] =  user_test.id

        context['questions'] = PSM25Question.objects.all()
        context['result_url'] = reverse('test-result', kwargs={'test_uuid': user_test.test_uuid})

        return context


class UserAnswerView(View):

    def post(self, request):
        try:
            test_attempt = UserTest.objects.get(id=self.request.session['test_id'])
            question_number = int(self.request.POST.get('question_number'))

            user_answer, _ = UserAnswer.objects.get_or_create(
                test_attempt=test_attempt,
                question_number=question_number
            )
            user_answer.answer = int(self.request.POST.get('score', 0))
            user_answer.save()

            if test_attempt.get_question_by_type().count() == question_number:
                test_attempt.finish_test()
                test_attempt.finished = True
                test_attempt.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'Error'}, status=400)


@method_decorator(login_required, name='dispatch')
class PSM25ResultView(TemplateView):

    template_name = 'psm/psm-results.html'

    def dispatch(self, request, *args, **kwargs):

        if 'test_id' not in self.request.session or self.request.session['test_id'] is None:
            return HttpResponseRedirect(reverse('psm25'))

        if UserTest.objects.get(id=self.request.session['test_id']).test_type != UserTest.PSM25_TEST:
            return HttpResponseRedirect(reverse('psm25'))

        if UserAnswer.objects.filter(test_attempt_id=self.request.session['test_id']).count() != \
                PSM25Question.objects.count():
            return HttpResponseRedirect(reverse('psm25'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_test = UserTest.objects.get(id=self.request.session['test_id'])
        score = user_test.get_test_result().score

        context['score'] = score
        context['message'] = f'Вы заработали {score}'
        context['link'] = reverse('test-result', kwargs={'test_uuid': user_test.test_uuid})
        return context


# endregion


class TailorTestView(BaseSessionView):
    template_name = 'tailor/tailor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_test = UserTest.objects.create(test_type=UserTest.TAILOR_TEST, user=self.request.user)
        self.request.session['test_id'] = user_test.id

        context['questions'] = TailorQuestion.objects.all()
        context['result_url'] = reverse('user-result', kwargs={'test_uuid': user_test.test_uuid})

        return context


@method_decorator(login_required, name='dispatch')
class TailorResultView(TemplateView):
    template_name = 'tailor/tailor_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_test = UserTest.objects.get(id=self.request.session['test_id'])
        score = user_test.get_test_result().score

        context['score'] = score
        context['message'] = f'Вы заработали {score}'
        context['link'] = reverse('test-result', kwargs={'test_uuid': user_test.test_uuid})
        return context


@method_decorator(login_required, name='dispatch')
class EmotionalBurnoutTestView(BaseSessionView):

    template_name = 'emotional_burnout/emotional_burnout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_test = UserTest.objects.create(test_type=UserTest.EMOTIONAL_BURNOUT_TEST, user=self.request.user)
        self.request.session['test_id'] = user_test.id

        context['questions'] = EmotionalBurnoutQuestion.objects.all()
        context['result_url'] = reverse('test-result', kwargs={'test_uuid': user_test.test_uuid})

        return context


@method_decorator(login_required, name='dispatch')
class EmotionalBurnoutResultView(TemplateView):
    template_name = 'emotional_burnout/emotional_burnout_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_test = UserTest.objects.get(id=self.request.session['test_id'])
        result_object = user_test.get_test_result()

        context['score'] = result_object.self_dissatisfaction
        context['message'] = f'Вы заработали {result_object.self_dissatisfaction}'
        context['link'] = reverse('test-result',  kwargs={'test_uuid': user_test.test_uuid})
        return context


class TestResultView(TemplateView):

    def get_template_names(self, *args, **kwargs):
        test = UserTest.objects.get(test_uuid=self.kwargs.get('test_uuid'))
        if test.test_type == UserTest.TAILOR_TEST:
            return 'tailor/tailor_result.html'
        elif test.test_type == UserTest.PSM25_TEST:
            return 'psm/psm-results.html'
        elif test.test_type == UserTest.EMOTIONAL_BURNOUT_TEST:
            return 'emotional_burnout/emotional_burnout_result.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        test = UserTest.objects.get(test_uuid=self.kwargs.get('test_uuid'))
        result_object = test.get_test_result()

        # TODO: Сюда запихнешь данные из контекстов соответстующих страниц результатов
        if test.test_type == UserTest.TAILOR_TEST:
            score = result_object.score
            context['score'] = score
            stress_level = 0
            if 15 <= score < 25:
                stress_level = 1
            elif 25 <= score < 40:
                stress_level = 2
            elif 40 <= score <= 50:
                stress_level = 3
            context['stress_level'] = stress_level

        elif test.test_type == UserTest.PSM25_TEST:
            context['score'] = result_object.score
            context['message'] = f'Вы заработали {result_object.score}'
        elif test.test_type == UserTest.EMOTIONAL_BURNOUT_TEST:
            context['score'] = result_object.self_dissatisfaction
            context['message'] = f'Вы заработали {result_object.self_dissatisfaction}'
        return context


class UserResultView(TemplateView):

    template_name = 'user_result.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise HttpResponseForbidden

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(UserResultView, self).get_context_data(*args, **kwargs)

        context['user'] = UserExtended.objects.get(id=self.kwargs.get('user_id'))

        context['user_tests'] = UserTest.objects.filter(user=context['user'], finished=True)

        return context
