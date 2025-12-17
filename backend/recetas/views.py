from rest_framework.decorators import APIView
from django.http.response import JsonResponse   
from http import HTTPStatus 
from django.http import Http404
from django.utils.text import slugify
from .models import Receta
from .serializer import *
from helpers.response import ResponseHandler
from datetime import datetime as dateTime
from django.core.files.storage import FileSystemStorage

# Create your views here.
class Class1(APIView):
    def get(self, request):
        try:
            data = Receta.objects.order_by('-id').all()
            data_serialized = RecetaSerializer(data, many=True)
            return ResponseHandler.success(message="Recetas obtenidas correctamente", data=data_serialized.data)
        except Exception as e:
            return ResponseHandler.create(message="Error al obtener las recetas", error=str(e))
        
    def post(self, request):
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return ResponseHandler.error(message="El campo nombre es obligatorio")
        if request.data.get("tiempo") == None or not request.data["tiempo"]:
            return ResponseHandler.error(message="El campo tiempo es obligatorio")
        if request.data.get("descripcion") == None or not request.data["descripcion"]:
            return ResponseHandler.error(message="El campo descripcion es obligatorio")
        if request.data.get("categoria_id") == None or not request.data["categoria_id"]:
            return ResponseHandler.error(message="El campo categoria es obligatorio")
        
        try:
            categoria = Categoria.objects.filter(pk=request.data["categoria_id"]).get()
        except Categoria.DoesNotExist:
            return ResponseHandler.error(message="La categoria no existe")
        
        if Receta.objects.filter(nombre=request.data["nombre"]).exists():
            return ResponseHandler.error(message="Ya existe una receta con ese nombre")
        
        file = FileSystemStorage()
        try:
            foto = f"{dateTime.timestamp(dateTime.now())}_{request.FILES['foto'].name}"
        except Exception:
            return ResponseHandler.error(message="Debe subir una imagen de la receta")
        
        if request.FILES['foto'].content_type == "image/jpeg" or request.FILES['foto'].content_type == "image/png":
            try:
                file.save(f"recetas/{foto}", request.FILES["foto"])
                file.url(request.FILES["foto"])
            except Exception as e:
                return ResponseHandler.error(message="Error al subir la imagen", error=str(e))

            try:
                Receta.objects.create(
                    nombre=request.data["nombre"],
                    tiempo = request.data["tiempo"],
                    descripcion = request.data["descripcion"],
                    categoria_id = request.data["categoria_id"],
                    fecha = dateTime.now(),
                    foto = foto
                )
                return ResponseHandler.success(message="Receta creada correctamente")
            except Exception as e:
                return ResponseHandler.error(message="Error al crear la receta", error=str(e))
        return ResponseHandler.error(message="El formato de la imagen no es válido, solo se aceptan jpg y png")


class Class2(APIView):
    def get(self, request, id):
        try:
            data = Receta.objects.filter(id=id).get()
            dataSerialized = RecetaSerializer(data)
            return ResponseHandler.success(message="Receta obtenida correctamente", data=dataSerialized.data)
        except Receta.DoesNotExist:
            return ResponseHandler.error(message="Receta no encontrada")
        
    def put(self, request, id):
        try:
            data = Receta.objects.filter(id=id).get()
        except Receta.DoesNotExist:
            return ResponseHandler.error(message="Receta no encontrada")
        
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return ResponseHandler.error(message="El campo nombre es obligatorio")
        if request.data.get("tiempo") == None or not request.data["tiempo"]:
            return ResponseHandler.error(message="El campo tiempo es obligatorio")
        if request.data.get("descripcion") == None or not request.data["descripcion"]:
            return ResponseHandler.error(message="El campo descripcion es obligatorio")
        if request.data.get("categoria_id") == None or not request.data["categoria_id"]:
            return ResponseHandler.error(message="El campo categoria es obligatorio")
        
        try:
            categoria = Categoria.objects.filter(pk=request.data["categoria_id"]).get()
        except Categoria.DoesNotExist:
            return ResponseHandler.error(message="La categoria no existe")
        
        try:
            Receta.objects.filter(id=id).update(
                nombre=request.data["nombre"],
                slug = slugify(request.data["nombre"]),
                tiempo = request.data["tiempo"],
                descripcion = request.data["descripcion"],
                categoria_id = request.data["categoria_id"]
            )
            return ResponseHandler.success(message="Receta actualizada correctamente")
        except Exception as e:
            return ResponseHandler.error(message="Error al actualizar la receta", error=str(e))