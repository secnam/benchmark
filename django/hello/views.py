from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View


class HelloView(View):
    def dispatch(request, *args, **kwargs):
        return HttpResponse('Hello World!')
