from django.urls import path
from .views import *

urlpatterns = [
    path("categorias", Class1.as_view()),
    path("categorias/<int:id>", Class2.as_view()),
]