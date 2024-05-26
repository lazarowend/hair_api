from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . models import Barbershop
from . serializers import BarbershopModelSerializer


class ListCreateBarbershopView(ListCreateAPIView):
    model = Barbershop
    serializer_class = BarbershopModelSerializer


class RetriveUpdateDestroyBarbershopView(RetrieveUpdateDestroyAPIView):
    model = Barbershop
    serializer_class = BarbershopModelSerializer
