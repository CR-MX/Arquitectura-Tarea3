#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------
# Archivo: views.py
#
# Implementación de Arquitecturas Microservicios.
# Autor(es): Perla Velasco & Jorge Alfonso Solís.
# Version: 1.0.0 Marzo 2021
#
# Descripción:
#   En este archivo se definen las vistas del sistema.
#
#   A continuación se describen los métodos que se implementaron en este archivo:
#
#                                               Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |                       |
#           |                        |                          |  - Obtiene la lista   |
#           |         list()         |  - request: datos de     |    de mensajes.       |
#           |                        |    la solicitud.         |                       |
#           |                        |                          |                       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |                       |
#           |                        |                          |  - Permite crear un   |
#           |        create()        |  - request: datos de     |    mensaje nuevo.     |
#           |                        |    la solicitud.         |                       |
#           |                        |                          |                       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |                       |
#           |                        |    la solicitud.         |  - Obtiene un mensaje |
#           |       retrieve()       |                          |    en específico de   |
#           |                        |  - pk: identificador del |    acuerdo con la pk. |
#           |                        |    mensaje.              |                       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |                       |
#           |                        |    la solicitud.         |  - Actualiza un mensa-|
#           |        update()        |                          |    je en específico de|
#           |                        |  - pk: identificador del |    acuerdo con la pk. |
#           |                        |    mensaje.              |                       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - request: datos de     |                       |
#           |                        |    la solicitud.         |  - Elimina un mensaje |
#           |       destroy()        |                          |    en específico de   |
#           |                        |  - pk: identificador del |    cuerdo con la pk.  |
#           |                        |    mensaje.              |                       |
#           +------------------------+--------------------------+-----------------------+
#
#--------------------------------------------------------------------------------------------------


from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order,OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

class OrderViewSet(viewsets.ViewSet):

    # Método que se accede por la URL /django
    def list(self, request):
        # Se obtiene la lista de mensajes
        order = Order.objects.all()
        # Se crea el serializer y se envía como response
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    # Método que se accede por la URL /django
    def create(self, request):
        # Se crea el serializer con los datos recibidos
        serializer = OrderSerializer(data=request.data)
        # Se verifica si el serializer es válido
        serializer.is_valid(raise_exception=True)
        # Se guarda el serializer
        serializer.save()
        # Se envía la respuesta de la solicitud
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Método que se accede por la URL /django/<str:pk>
    def retrieve(self, request, pk=None):
        # Se obtiene el mensaje con ayuda del pk recibido
        message = Order.objects.get(id=pk)
        # Se crea el serializer
        serializer = OrderSerializer(message)
        # Se envía la respuesta a la solicitud
        return Response(serializer.data)

    # Método que se accede por la URL /django/<str:pk>
    def update(self, request, pk=None): 
        # Se obtiene el mensaje con ayuda del pk recibido
        message = Order.objects.get(id=pk)
        # Se crea el serializer con los datos recibidos
        serializer = OrderSerializer(instance=message, data=request.data)
        # Se verifica si el serializer es válido
        serializer.is_valid(raise_exception=True)
        # Se guarda el serializer
        serializer.save()
        # Se envía la respuesta a la solicitud
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # Método que se accede por la URL /django/<str:pk>
    def destroy(self, request, pk=None):
        # Se obtiene el mensaje con ayuda del pk recibido
        message = Order.objects.get(id=pk)
        # Se procede a eliminar el mensaje
        message.delete()
        # Se envía la respuesta a la solicitud
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderItemViewSet(viewsets.ViewSet):

    # Método que se accede por la URL /django
    def list(self, request):
        # Se obtiene la lista de mensajes
        orderItem = OrderItem.objects.all()
        # Se crea el serializer y se envía como response
        serializer = OrderItemSerializer(orderItem, many=True)
        return Response(serializer.data)

    # Método que se accede por la URL /django
    def create(self, request):
        # Se crea el serializer con los datos recibidos
        serializer = OrderItemSerializer(data=request.data)
        # Se verifica si el serializer es válido
        serializer.is_valid(raise_exception=True)
        # Se guarda el serializer
        serializer.save()
        # Se envía la respuesta de la solicitud
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Método que se accede por la URL /django/<str:pk>
    def retrieve(self, request, pk=None):
        # Se obtiene el mensaje con ayuda del pk recibido
        message = OrderItem.objects.get(id=pk)
        # Se crea el serializer
        serializer = OrderItemSerializer(message)
        # Se envía la respuesta a la solicitud
        return Response(serializer.data)

    # Método que se accede por la URL /django/<str:pk>
    def update(self, request, pk=None): 
        # Se obtiene el mensaje con ayuda del pk recibido
        message = OrderItem.objects.get(id=pk)
        # Se crea el serializer con los datos recibidos
        serializer = OrderItemSerializer(instance=message, data=request.data)
        # Se verifica si el serializer es válido
        serializer.is_valid(raise_exception=True)
        # Se guarda el serializer
        serializer.save()
        # Se envía la respuesta a la solicitud
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # Método que se accede por la URL /django/<str:pk>
    def destroy(self, request, pk=None):
        # Se obtiene el mensaje con ayuda del pk recibido
        message = OrderItem.objects.get(id=pk)
        # Se procede a eliminar el mensaje
        message.delete()
        # Se envía la respuesta a la solicitud
        return Response(status=status.HTTP_204_NO_CONTENT)