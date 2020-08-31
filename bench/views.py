import json

from django.db import connection
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import HttpResponse

from .models import Chair


class HelloView(View):
    """
    HELLOOOOOOOOOOOOOOOOOOOOO!
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World!')


class SomeTemplateView(TemplateView):
    """
    Some Template!
    """

    template_name = 'bench/some_template.html'


class ChairListJsonView(View):
    """
    Sends chairs as a JSON.
    """
    def get(self, request, *args, **kwargs):
        chairs = Chair.objects.values()
        return HttpResponse(json.dumps(list(chairs)))
