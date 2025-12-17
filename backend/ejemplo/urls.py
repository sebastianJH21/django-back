from django.urls import path
from .views import Class_ejemplo, Class_ejemploParametros, Class_ejemploUpload

urlpatterns = [
    path("ejemplo", Class_ejemplo.as_view()), 
    path("ejemplo/<int:id>", Class_ejemploParametros.as_view()),
    path("ejemplo-upload", Class_ejemploUpload.as_view())
]