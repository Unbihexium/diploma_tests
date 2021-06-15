from django.shortcuts import render, reverse
from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponseRedirect

from uuid import uuid4


from psychological_tests.models import PSM25Question, PSM25UserAnswer


# Create your views here.
def main(request, *args, **kwargs):
    return render(request, 'base.html')

# region psm
class PSM25TestView(TemplateView):

    template_name = 'psm/psm25.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['questions'] = PSM25Question.objects.all()

        return context

    def dispatch(self, *args, **kwargs):
        self.request.session['test_id'] = str(uuid4())

        return super().dispatch(*args, **kwargs)


class PSM25UserAnswerView(View):

    def post(self, request):
        PSM25UserAnswer.objects.create(
            test_id=request.session['test_id'],
            answer=int(request.POST.get('score', 0)),
        )
        return JsonResponse({'status': 'success'})


class PSM25ResultView(TemplateView):

    template_name = 'psm/psm-results.html'

    def dispatch(self, request, *args, **kwargs):

        if 'test_id' not in request.session:
            return HttpResponseRedirect(reverse('psm25'))

        if PSM25UserAnswer.objects.filter(test_id=request.session['test_id']).count() != PSM25Question.objects.count():
            return HttpResponseRedirect(reverse('psm25'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_answers = PSM25UserAnswer.objects.filter(test_id=self.request.session['test_id'])
        score = sum(map(lambda answer: answer.answer, user_answers))
        context['score'] = score
        context['message'] = f'Вы заработали {score}'
        return context
# endregion
