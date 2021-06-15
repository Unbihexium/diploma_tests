from django.shortcuts import render
from django.views.generic import TemplateView

from uuid import uuid4


from psychological_tests.models import PSM25Question


# Create your views here.
def main(request, *args, **kwargs):
    return render(request, 'base.html')


class PSM25TestView(TemplateView):

    template_name = 'psm25.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['questions'] = PSM25Question.objects.all()

        return context

    def dispatch(self, *args, **kwargs):
        self.request.session['test_id'] = str(uuid4())

        return super().dispatch(*args, **kwargs)
