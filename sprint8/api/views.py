from http import client
from django.shortcuts import render
from api.models import *
from api.serializers import *
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

    def put(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaldoCuenta(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
         cuenta = Cuenta.objects.filter(pk=pk).first()
         serializer = CuentasSerializer(cuenta)
         if cuenta:
             return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class MontoPrestamo(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
         prestamo = Prestamo.objects.filter(pk=pk).first()
         serializer = PrestamoSerializer(prestamo)
         if prestamo:
            return Response(serializer.data, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class PrestamosSucursal(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TarjetasCredito(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #def get(self, request, pk):
    #    tarjeta = Tarjeta.objects.filter(cliente_cuenta=pk).first()
     #   print(tarjeta)
     #   serializer = TarjetaSerializer(tarjeta)
    #    if tarjeta:
    #        return Response(serializer.data, status=status.HTTP_200_OK)
    #    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND) """

class PedirPrestamo(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AnularPrestamo(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ModificarDireccion(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        dir = Direcciones.objects.all(pk)
        serializer = DireccionesSerializer(dir)
        if dir:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    """ def put(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """

class Sucursales(APIView):
    ermission_classes = [permissions.IsAuthenticatedOrReadOnly]
   # def get(self, request):
    #     sucursal = Sucursal.objects.all().order_by('branch_id')
      #   serializer = SucursalSerializer(sucursal)
      #   if sucursal:
       #      return Response(serializer.data, status=status.HTTP_200_OK)
      #   return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
     

# class UserList(generics.ListAPIView):
   #  queryset = User.objects.all()
   #  serializer_class = UserSerializer 