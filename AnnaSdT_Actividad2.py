#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos las librerias necesarias
import MySQLdb
import os
from gi.repository import Gtk


# Establecemos la conexion con la base de datos y creamos unas filas en la tabla para empezar a trabajar
conexion = MySQLdb.connect(host='localhost', user='familia',passwd='anna', db='Familia')
cursor = conexion.cursor(MySQLdb.cursors.DictCursor)

# Clase
class Handler:
    def __init__(self):
        self.__valor = True

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print("Hello World!")


# Parte principal dep programa
builder = Gtk.Builder()
builder.add_from_file("AnnaSdT_Actividad2.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
