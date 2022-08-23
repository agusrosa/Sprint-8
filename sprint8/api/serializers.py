from asyncio.streams import _ClientConnectedCallback
from dataclasses import field
from rest_framework import serializers
from .models import Dato

class DatosSerializar(serializers.ModelSerializer):
    class Meta:
        model=Dato
        fields="__all__"
        read_only_fields=(
            "id",
            "creacion",
            "actualizacion",
            "saldo_cuenta"
        )