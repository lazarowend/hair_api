from rest_framework import serializers
from . models import Barbershop


class BarbershopModelSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Barbershop
        fields = '__all__'