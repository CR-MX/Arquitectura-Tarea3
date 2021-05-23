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

from .views import OrderViewSet,OrderItemViewSet

urlpatterns = [
    path('orden', OrderViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('orden/<str:pk>', OrderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('ordenitem', OrderItemViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('ordenitem/<str:pk>', OrderItemViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))


]
