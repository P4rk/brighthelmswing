from django.http import HttpResponse

# Create your views here.
from django.template import loader


def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def space(request):
    template = loader.get_template('safe-spaces.html')
    context = {}
    return HttpResponse(template.render(context, request))
