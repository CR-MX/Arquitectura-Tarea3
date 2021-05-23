# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: gui.py
# Implementación de Arquitecturas Micro Servicios.
# Autor(es): Perla Velasco & Jorge Alfonso Solís.
# Version: 1.0 Marzo 2021
# Descripción:
#
#   Este archivo define la interfaz gráfica del usuario. Recibe un parámetro que define el 
#   Microservicio que se desea utilizar.
#   
#                                             gui.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Porporcionar la in-  | - Consume servicios    |
#           |          GUI          |    terfaz gráfica con la|   para proporcionar    |
#           |                       |    que el usuario hará  |   información al       |
#           |                       |    uso del sistema.     |   usuario.             |
#           +-----------------------+-------------------------+------------------------+
#

from flask import Flask, render_template
import json, requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Se definen las llaves de cada microservicio
# Catalogos -> Category
key_m1 = "28bd3fe480ca4270a066f5221f572975"
headers_m1 = {"authorization": key_m1}
# Catalogos -> product
key_m4 = "4113ec56cbcd4e1ab5f86dcaaa500841"
headers_m4 = {"authorization": key_m4}
# Carritos -> carrito
key_m2 = "f76b6854e37c49699ce7bbae8ca63b39"
header_m2 = {"authorization": key_m2}
# Ordenes -> orden
key_m3 = "66ecc7405fbe4f39acebfe341fe3e55b"
header_m3 = {"authorization": key_m3}
# Ordenes -> ordenitem
key_m5 = "66ecc7405fbe4f39acebfe341fe3e55b"
header_m5 = {"authorization": key_m5}


# Se definen las url para cada micro servicio.
# Se reemplaza el 127.0.0.1 del localhost por host.docker.internal para hacer la conexión
# con los microservicios dentro de los contenedores de Docker.

# Url para category
url_microservice1 = 'http://host.docker.internal:8080/catalogos/category'
# Url para product
url_microservice4 = 'http://host.docker.internal:8080/catalogos/product'
# Url para carrito
url_microservice2 = 'http://host.docker.internal:8080/carritos/carrito'
# Url para orden
url_microservice3 = 'http://host.docker.internal:8080/ordenes/orden'
# Url para ordenitem
url_microservice5 = 'http://host.docker.internal:8080/ordenes/ordenitem'
'''
catalog_categori
    id,name,slug
catalog_product
    id,name,slug,image,description,price,stock,avaliable, created, 
    id,name,slug,image,price,stock,avaliable, created, updated,category_id

orders_order
    id,first_name,last_name,email,addres,postal_code,city,created,updated,paid
orders_orderitem
    id,price,quantity,order_id,product_id
'''


# Método que muestra la página de inicio del sistema
@app.route("/", defaults={'api': None}, methods=['GET'])
@app.route("/<api>", methods=['GET'])
def index(api):

    # Se verifica si se recibió la variable api
    if api:

        if int(api) == 1:
            # Se llama al microservicio enviando como parámetro la url y el header
            ms1 = requests.get(url_microservice1, headers=headers_m1)
            # Se convierte la respuesta a json
            json = ms1.json()
            # Se llama al microservicio enviando como parámetro la url y el header
            ms1 = requests.get(url_microservice4, headers=headers_m4)
            # Se convierte la respuesta a json
            json += ms1.json()
            # Se crea el json que será enviado al template
            json_result = {'id': json, 'image':json}

        elif int(api) == 2:
            # Se llama al microservicio enviando como parámetro la url y el header
            ms2 = requests.get(url_microservice2, headers=header_m2)
            # Se convierte la respuesta a json
            json = ms2.json()
            # Se crea el json que será enviado al template
            json_result = {'ms2': json}
        elif int(api) == 3:
            # Se llama al microservicio enviando como parámetro la url y el header 
            ms3 = requests.get(url_microservice3, headers=header_m3)
            # Se convierte la respuesta a json
            json = ms3.json()
            # Se crea el json que será enviado al template
            json_result = {'ms3': json}
        
        return render_template("index.html", result=json_result)
    
    # Si no se recibe, simplemente se regresa el template index.html sin datos.
    else:
        json_result = {}
        return render_template("index.html", result=json_result)
# otras cosas
@app.route("/cart/detail")
def cdetail():
    return render_template("cart/detail.html")

@app.route("/order/create")
def create():
    return render_template("order/create.html")

@app.route("/order/created")
def created():
    return render_template("order/created.html")

@app.route("/order/list")
def olist():
    return render_template("order/list.html")

@app.route("/orders/orderitemlist")
def orderitemlist():
    return render_template("orders/orderitem_list.html")

@app.route("/orders/orderlist")
def orderlist():
    return render_template("orders/order_list.html")

@app.route("/orders/delete")
def deleteorders():
    return render_template("orders/delete.html")

@app.route("/orders/confirmcancel")
def confirmcancel():
    return render_template("orders/confirm_cancel_product.html")

@app.route("/products/list")
def plist():
    return render_template("products/list.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')