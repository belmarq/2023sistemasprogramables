from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


from webapp.models import Cliente, ClienteSensor

clientes = {}
lampara = 2
class Home(APIView):
    def get(self, request):
        cdx = {
            #'titulo':'Enlaces',
            #'URL':request.build_absolute_uri('/ledoff'),
            #'URL': request.META.get('HTTP_HOST'),
            #'IP':request.META.get('REMOTE_ADDR'),
            #'puerto':request.META['SERVER_PORT'],
            #'todos': request.META.items(),
            #'todos': request.POST,
            'clientes':Cliente.objects.all(),
            'cliente':Cliente.objects.first(),
        }
        return render(request, 'index.html', cdx)

    def post(self, request):
        global lampara
        lampara2 = int(request.POST.get('lampara'))
        lampara = lampara2
        return redirect('home')




class GetIP(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip:
            ip = user_ip.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        port = request.META.get('REMOTE_PORT')
        return HttpResponse(f"Cliente IP: {ip}, Puerto: {port}")

    def post(self, request):
        global lampara
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip:
            ip = user_ip.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        port = request.META.get('REMOTE_PORT')
        valor = request.POST.get('valor')
        sensor = request.POST.get('sensor')
        sensor_cliente = ClienteSensor.objects.filter(sensor=int(sensor)).first()
        id_cliente = 0
        if sensor_cliente:
            id_cliente=sensor_cliente.cliente.id
        return JsonResponse({'lampara':lampara, 'valor_enviado':valor, 'ip':ip, 'puerto':port, 'cliente':id_cliente})