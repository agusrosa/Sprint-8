from http import client
from django.shortcuts import render
from api.models import Cliente,Sucursal,Empleado,Direccion,Tiposclientes,Prestamo,TipoCuenta,Cuenta,MarcaTarjeta,Tarjeta,User
from api.serializers import ClienteSerializer,PrestamoSerializer,CuentasSerializer,SucursalSerializer,DireccionesSerializer,TarjetaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions


# Create your views here.
class DatosCliente (APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente)
        if cliente:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class SaldoCuenta(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
         cuenta = Cuenta.objects.filter(pk=pk).first()
         serializer = CuentasSerializer(cuenta)
         if cuenta:
             return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class MontoPrestamo(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PrestamosSucursal(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TarjetasCredito(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PedirPrestamo(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AnularPrestamo(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ModificarDireccion(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Sucursales(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class UserList(generics.ListAPIView):
   #  queryset = User.objects.all()
   #  serializer_class = UserSerializer 