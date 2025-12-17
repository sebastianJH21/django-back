from rest_framework import serializers
from .models import *
from dotenv import load_dotenv
import os

class RecetaSerializer(serializers.ModelSerializer):
    categoria = serializers.ReadOnlyField(source='categoria.nombre')
    fecha = serializers.DateTimeField(format= "%d/%m/%Y")
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = Receta
        # fields = '__all__'
        fields = ('id', 'nombre', 'slug', 'tiempo', 'descripcion', 'fecha', 'categoria', 'categoria_id', 'imagen')
    
    def  get_imagen(self, obj):
        return f"{os.getenv('BASE_URL')}/upload/recetas/{obj.foto}"