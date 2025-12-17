from django.urls import path
from .views import *

urlpatterns = [
    path("recetas", Class1.as_view()),
    path("recetas/<int:id>", Class2.as_view()),
]