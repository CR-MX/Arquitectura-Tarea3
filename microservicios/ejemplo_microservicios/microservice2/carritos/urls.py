#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: urls.py
#
# Implementación de Arquitecturas Microservicios.
# Autor(es): Perla Velasco & Jorge Alfonso Solís.
# Version: 1.0.0 Marzo 2021
#
# Descripción:
#   En este archivo se definen las urls de la app hello_django.
#
#-------------------------------------------------------------------------

from django.urls import path

from .views import MessageViewSet

urlpatterns = [
    path('carrito', MessageViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('carrito/<str:pk>', MessageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))

]
