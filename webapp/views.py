from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

solicitudes = {}

class Home(View):
    def get(self, request):
        global solicitud
        cdx = {
            'titulo':'Enlaces',
            'URL':request.build_absolute_uri('/ledoff'),
            #'URL': request.META.get('HTTP_HOST'),
            'IP':request.META.get('REMOTE_ADDR'),
            'puerto':request.META['SERVER_PORT'],
            #'todos': request.META.items(),
            #'todos': request.POST,
            'todos': request.POST,
        }
        return render(request, 'index.html', cdx)