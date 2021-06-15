from django.shortcuts import render, reverse
from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponseRedirect

from uuid import uuid4

from psychological_tests.models import TailorQuestion, PSM25Question, UserAnswer


# Create your views here.
def main(request, *args, **kwargs):
    return render(request, 'base.html')


class BaseSessionView(TemplateView):

    def dispatch(self, *args, **kwargs):
        self.request.session['test_id'] = str(uuid4())
        return super().dispatch(*args, **kwargs)


# region psm
class PSM25TestView(BaseSessionView):
    template_name = 'psm/psm25.html'

    def dispatch(self, *args, **kwargs):
        self.request.session['test'] = 'psm25'
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['questions'] = PSM25Question.objects.all()
        context['result_url'] = reverse('psm25-result')

        return context


class UserAnswerView(View):

    def post(self, request):
        UserAnswer.objects.create(
            test_id=request.session['test_id'],
            answer=int(request.POST.get('score', 0)),
        )
        return JsonResponse({'status': 'success'})


class PSM25ResultView(TemplateView):

    template_name = 'psm/psm-results.html'

    def dispatch(self, request, *args, **kwargs):

        if 'test_id' not in request.session:
            return HttpResponseRedirect(reverse('psm25'))

        if self.request.session.get('test', '') != 'psm25':
            return HttpResponseRedirect(reverse('psm25'))

        if UserAnswer.objects.filter(test_id=self.request.session['test_id']).count() != PSM25Question.objects.count():
            return HttpResponseRedirect(reverse('psm25'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_answers = UserAnswer.objects.filter(test_id=self.request.session['test_id'])
        score = sum(map(lambda answer: answer.answer, user_answers))
        context['score'] = score
        context['message'] = f'Вы заработали {score}'
        return context


# endregion


class TailorTestView(BaseSessionView):
    template_name = 'tailor/tailor.html'

    def dispatch(self, *args, **kwargs):
        self.request.session['test'] = 'tailor'
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['questions'] = TailorQuestion.objects.all()
        context['result_url'] = reverse('tailor-result')

        return context


class TailorResultView(TemplateView):
    template_name = 'tailor/tailor_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Test msg'
        return context
