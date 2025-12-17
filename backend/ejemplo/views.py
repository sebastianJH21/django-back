from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse, Http404
from http import HTTPStatus
from django.core.files.storage import FileSystemStorage
import os
from datetime import datetime
# from rest_framework.response import Response
# Create your views here.

class Class_ejemplo(APIView):

    def get(self, request):
        # return HttpResponse(f"Metodo GET: id={request.GET.get('id', None)}, slud={request.GET.get('slug', None)}")
        # return Response({"status": "ok", "metodo": "GET"})
        return JsonResponse({"status": "ok", "metodo": "GET"}, status=HTTPStatus.OK)
    
    def post(self, request):
        if request.data.get("email") == None or request.data.get("password") == None:
            # return Response({"status": "error", "metodo": "POST", "detalle": "Faltan parametros"})
            raise Http404
        

        return JsonResponse({"status": "ok", "metodo": "POST", "email": request.data.get("email", None), "password": request.data.get("password", None)}, status=HTTPStatus.CREATED)


class Class_ejemploParametros(APIView):
    def get(self, request, id):
        return HttpResponse(f"Metodo GET: parametro id = {id}")
    
    def put(self, request, id):
        return HttpResponse(f"Metodo PUT: parametro id = {id}")
    
    def delete(self, request, id):
        return HttpResponse(f"Metodo DELETE: parametro id = {id}")
    

class Class_ejemploUpload(APIView):

    def post(self, request):
        fs = FileSystemStorage()
        date = datetime.now()
        file = f"{datetime.timestamp(date)}_{request.FILES['file'].name}"
        fs.save(f"ejemplo/{file}", request.FILES["file"])
        fs.url(request.FILES["file"])
        return JsonResponse({"status": "ok", "metodo": "POST", "detalle": "Archivo subido correctamente"}, status=HTTPStatus.CREATED)