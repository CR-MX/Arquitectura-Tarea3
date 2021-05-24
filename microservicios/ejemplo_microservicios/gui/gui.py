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
key_m1 = "7802864422a64577880e519dc003c51c"
header_m1 = {"authorization": key_m1}
# Catalogos -> product
key_m4 = "9c97fc13aacf49a7b187bc7b88abc88c"
header_m4 = {"authorization": key_m4}
# Carritos -> carrito
key_m2 = "1279c487851b4a6facec1a8099c30d05"
header_m2 = {"authorization": key_m2}
# Ordenes -> orden
key_m3 = "a53605cc91f542f7a159908580e4caf0"
header_m3 = {"authorization": key_m3}
# Ordenes -> ordenitem
key_m5 = "0bf6749ffa034ba68aba77f68214f523"
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

# pagina principal con categorias e items
@app.route("/products/list")
def plist():
    # Categoria
    categoria = requests.get(url_microservice1, headers=header_m1)
    # Se convierte la respuesta a json
    json1 = categoria.json()
    # Product
    producto = requests.get(url_microservice4, headers=header_m4)
    # Se convierte la respuesta a json
    json2 = producto.json()
    # Se crea el json que será enviado al template
    
    return render_template("products/list.html",result={'categoria': json1,'producto':json2})

# redireccion de inicio
@app.route("/", methods=['GET'])
def index():
    #Redirecciona a products/list.html
    return plist()

# Lista de productos
@app.route("/order/list")
def olist():
    # order
    order = requests.get(url_microservice3, headers=header_m3)
    # Se convierte la respuesta a json
    json3 = order.json()
    return render_template("order/list.html",result={'order': json3})

# Eliminar uno por uno
@app.route("/orders/orderitemlist")
@app.route("/orders/orderitemlist/<int:id>", methods=['GET'])

def orderitemlist(id):
    # order
    order = requests.get(url_microservice3, headers=header_m3)
    # Se convierte la respuesta a json
    # orderitem
    orderitem = requests.get(url_microservice5, headers=header_m5)

    # Se convierte la respuesta a json
    json4 = orderitem.json()
    return render_template("orders/order_list.html",id=id , result={'orderitem':json4})

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





@app.route("/orders/orderlist")
def orderlist():
    return render_template("orders/order_list.html")

@app.route("/orders/delete")
def deleteorders():#borra uno
    return render_template("orders/delete.html")

@app.route("/orders/confirmcancel")
def confirmcancel():#borratodo
    return render_template("orders/confirm_cancel_product.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')