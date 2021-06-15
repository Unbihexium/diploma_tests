from django.shortcuts import render

# Create your views here.
def test(request, *args, **kwargs):
    return render(request, 'base.html')