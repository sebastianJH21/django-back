from rest_framework.decorators import APIView
from django.http.response import JsonResponse   
from http import HTTPStatus 
from django.http import Http404
from django.utils.text import slugify
from .models import *
from .serializer import *
# Create your views here.

class Class1(APIView):

    def get(self, request):
        data = Categoria.objects.order_by('-id').all()
        data_json = CategoriaSerializer(data, many=True)
        return JsonResponse({"status": "ok", "data": data_json.data}, status=HTTPStatus.OK)
        # return JsonResponse({"status": "ok", "data": data_json}, status=200)


    def post(self, request):
        if  request.data['nombre'] is None or not request.data['nombre']:
            return JsonResponse({"status": "error", "message": "El nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        try:
            Categoria.objects.create(nombre=request.data['nombre'])
            return JsonResponse({"status": "ok", "message": "Categoria creada correctamente"}, status=HTTPStatus.CREATED)
        except Exception as e:
            raise Http404


class Class2(APIView):
    def get(self, request, id):
        try:
            data = Categoria.objects.filter(id = id).get()
            dataSerializer = CategoriaSerializer(data)
            return JsonResponse({"data": dataSerializer.data}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
        
    def put(self, request, id):
        if request.data['nombre'] is None or not request.data['nombre']:
            return JsonResponse({"status": "error", "message": "El nombre es obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        
        try:
            data = Categoria.objects.filter(id = id).get()
            Categoria.objects.filter(id = id).update(nombre=request.data['nombre'], slug=slugify(request.data['nombre']))
            return JsonResponse({"status": "ok", "message": "Categoria actualizada correctamente"}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
    
    def delete(self, request, id):
        try: 
            data = Categoria.objects.filter(id = id).get()
            Categoria.objects.filter(id = id).delete()
            return JsonResponse({"status": "ok", "message": "Categoria eliminada correctamente"}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
        