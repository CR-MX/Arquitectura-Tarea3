#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: models.py
#
# Autor(es): Perla Velasco & Jorge Alfonso Solís.
# Version: 1.0.0 Marzo 2021
#
# Descripción:
#
#   En este archivo se definen los modelos para la app
#
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |  - Se indica los       |
#           |                       |  - Representa el        |    campos del modelo   |
#           |        Message        |    mensaje que regresa  |    así como sus pro-   |
#           |                       |    el micro servicio.   |    piedades.           |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#
#-------------------------------------------------------------------------

from django.db import models

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    # Clase Meta en donde se indican campos para ordenamiento.
    class Meta:
        ordering = ('-created',)

    # Método to String de la clase, la cual es representada por el campo 'id'.
    def __str__(self):
        return 'Order {}'.format(self.id)

    # Método que obtiene el costo total de la orden.
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.IntegerField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    # Método to String de la clase, la cual es representada por el campo 'id'.
    def __str__(self):
        return '{}'.format(self.id)

    # Método que obtiene el costo total del item de la orden.
    def get_cost(self):
        return self.price * self.quantity

