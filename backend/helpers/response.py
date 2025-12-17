from django.http import JsonResponse
from http import HTTPStatus


class ResponseHandler:
    def create(message="Registro Creado Exitosamente", data=None):
        return JsonResponse({
                "success": True, 
                "message": message, 
                "data": data,
            }, status=HTTPStatus.CREATED)
    
    def success(message="Proceso exitoso", data=None):
        return JsonResponse({
                "success": True, 
                "message": message, 
                "data": data,
            }, status=HTTPStatus.OK)
    

    def error(message="Ocurrió un error", data=None, error=None):
        return JsonResponse({
                "success": False, 
                "message": message, 
                "data": data,
                "error": error
            }, status=HTTPStatus.BAD_REQUEST)