#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importamos las librerias necesarias
import MySQLdb
import re
from gi.repository import Gtk


# Establecemos la conexion con la base de datos
conexion = MySQLdb.connect(host="localhost", user="familia",passwd="anna", db="Familia")
micursor = conexion.cursor(MySQLdb.cursors.DictCursor)

# Nos comunicamos con la interficie
class Handler:

    # Inicializar
    def __init__(self):
        # Inicializamos y llamamos a la interficie
        self.builder = Gtk.Builder()
        self.builder.add_from_file("AnnaSdT_Actividad2.glade")
        # Busca cual es la ultima id que ya estaba en la tabla para no repetir ids
        query= "SELECT * FROM DatosFamilia WHERE 1;"
        micursor.execute(query)
        registros = micursor.fetchall()
        if (len(registros)==0):
            self.numid = 0
        else:
            self.numid = int(registros[-1]["id"])
        # Lista de handlers
        self.handlers = {
        "cerrargeneral": self.cerrargeneral,
        "clickcrear": self.clickcrear,
        "clickver": self.clickver,
        "clickactualizar": self.clickactualizar,
        "clickborrar": self.clickborrar,
        "clickacerca": self.clickacerca,
        "cerrarcrear": self.cerrarcrear,
        "cerrarver": self.cerrarver,
        "cerraractualizar": self.cerraractualizar,
        "cerrarborrar": self.cerrarborrar,
        "cerraracerca": self.cerraracerca,
        "cerrarerrfecha": self.cerrarerrfecha,
        "cerrarerrtexto": self.cerrarerrtexto,
        "cerrarerrid": self.cerrarerrid,
        "cerrareditar": self.cerrareditar,
        "clicksicrear": self.clicksicrear,
        "clicksiborrar": self.clicksiborrar,
        "clicksiactualizar": self.clicksiactualizar,
        "clicksieditar": self.clicksieditar
        }
        self.builder.connect_signals(self.handlers)
        self.wgeneral = self.builder.get_object("wgeneral")
        self.wgeneral.show_all()
        self.wcrear = self.builder.get_object("wcrear")
        self.wver = self.builder.get_object("wver")
        self.wactualizar = self.builder.get_object("wactualizar")
        self.wborrar = self.builder.get_object("wborrar")
        self.wacerca = self.builder.get_object("wacerca")
        self.werrtexto = self.builder.get_object("werrtexto")
        self.werrfecha = self.builder.get_object("werrfecha")
        self.werrid = self.builder.get_object("werrid")
        self.weditar = self.builder.get_object("weditar")
        self.txver = self.builder.get_object("txver")
        self.enombre1 = self.builder.get_object("enombre1")
        self.efecha1 = self.builder.get_object("efecha1")
        self.elugar1 = self.builder.get_object("elugar1")
        self.eprofesion1 = self.builder.get_object("eprofesion1")
        self.eaficiones1 = self.builder.get_object("eaficiones1")
        self.eborid = self.builder.get_object("eborid")
        self.eactid = self.builder.get_object("eactid")
        self.enombre2 = self.builder.get_object("enombre2")
        self.efecha2 = self.builder.get_object("efecha2")
        self.elugar2 = self.builder.get_object("elugar2")
        self.eprofesion2 = self.builder.get_object("eprofesion2")
        self.eaficiones2 = self.builder.get_object("eaficiones2")

    # Cerrar ventana general
    def cerrargeneral(self, *args):
        Gtk.main_quit(*args)

# VENTANA PARA CREAR REGISTROS

    # Accion que ocurre al clicar "Crear" en la ventana general
    def clickcrear(self, wgeneral):
        self.wcrear.show()

    # Accion que ocurre al clicar "Crear" en la ventana de crear un registro
    def clicksicrear(self, wcrear):
        nombre = self.enombre1.get_text()
        fecha = self.efecha1.get_text()
        lugar = self.elugar1.get_text()
        profesion = self.eprofesion1.get_text()
        aficiones = self.eaficiones1.get_text()
        # Si hay un campo vacio o el formato de fecha es incorrecto, lanza la ventana error de texto o error de fecha; si no, inserta el registro
        if len(nombre)==0 or len(lugar)==0 or len(profesion)==0 or len(aficiones)==0 or len(fecha)==0:
            self.werrtexto.show()
        elif not re.search("(19|20)\d{2}[-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])",fecha): 
            self.werrfecha.show()
        else:
            self.numid = self.numid+1
            query= "INSERT INTO DatosFamilia (id,Nombre,FechaNacimiento,LugarResidencia,Profesion,Aficiones) VALUES ( " + str(self.numid) + ",\"" + nombre + "\",\""+ fecha +"\",\"" + lugar +"\",\"" + profesion +"\",\"" + aficiones +"\");"
            micursor.execute(query)
            conexion.commit()
            self.enombre1.set_text("")
            self.efecha1.set_text("")
            self.elugar1.set_text("")
            self.eprofesion1.set_text("")
            self.eaficiones1.set_text("")
            self.wcrear.hide()

    # Cerrar la ventana de crear
    def cerrarcrear(self, *args):
        self.enombre1.set_text("")
        self.efecha1.set_text("")
        self.elugar1.set_text("")
        self.eprofesion1.set_text("")
        self.eaficiones1.set_text("")
        self.wcrear.hide()        
        return True

# VENTANA PARA VER LA TABLA

    # Accion que ocurre cuando clicamos "Ver" en la ventana general
    def clickver(self, wgeneral):
        self.wver.show()
        self.wver.show_all()
        query = "SELECT * FROM DatosFamilia WHERE 1"
        micursor.execute(query)
        registros = micursor.fetchall()
        tabla = "ID\t|\tNOMBRE\t\t\t|\tNACIMIENTO\t|\tCIUDAD\t\t\t|\tPROFESION\t|\tAFICIONES\t\t"
        tabla = tabla + "\n------------------------------------------------------------------------------------------------------------------"
        tabla = tabla + "------------------------------------------------------------------------------------------------------------------"
        for registro in registros:
            tabla = tabla + "\n" + str(registro["id"]) + "\t|\t" + registro["Nombre"] + "\t\t\t|\t" + str(registro["FechaNacimiento"])+ "\t|\t" + registro["LugarResidencia"] + "\t\t|\t" + registro["Profesion"] + "\t|\t" + registro["Aficiones"]
        self.txver.get_buffer().set_text(tabla)
        return True
    # Cerrar la ventana ver
    def cerrarver(self, *args):
        self.wver.hide()        
        return True

# VENTANA PARA ACTUALIZAR UN REGISTRO

    # Accion que ocurre cuando clicamos "Actualizar" en la ventana general
    def clickactualizar(self, wgeneral):
        self.wactualizar.show()

    # Accion que ocurre cuando clicamos "Actualizar" en la ventana de actualizar un registro
    def clicksiactualizar(self, wactualizar):
        actid = self.eactid.get_text()
        # Comprueba que la id introducida es un digito; si no, lanza la ventana error de id
        if not re.search("\d+",actid):
            self.werrid.show()
        else:
            # Si la id introducida no esta en la tabla lanza error de id; si esta, lanza la ventana "Editar" para editar los campos
            actid = int(actid)
            query= "SELECT * FROM DatosFamilia WHERE 1;"
            micursor.execute(query)
            registros = micursor.fetchall()
            idok = 0
            for registro in registros:
                idok = idok + (registro["id"]==actid)
            if (idok==0):
                self.werrid.show()
            else:
                # Variable con la id a editar que enviaremos a la ventana de editar campos de registro
                self.ideditar = actid
                # Pre-rellena los campos a editar con los valores actuales para facilitar la edicion
                query= "SELECT * FROM DatosFamilia WHERE id = " + str(actid) + ";"
                micursor.execute(query)
                conexion.commit()
                registro = micursor.fetchall()
                self.enombre2.set_text(registro[0]["Nombre"])
                self.efecha2.set_text(str(registro[0]["FechaNacimiento"]))
                self.elugar2.set_text(registro[0]["LugarResidencia"])
                self.eprofesion2.set_text(registro[0]["Profesion"])
                self.eaficiones2.set_text(registro[0]["Aficiones"])
                self.weditar.show()
                self.eactid.set_text("")
                self.wactualizar.hide()

    # Cerrar la ventana actualizar
    def cerraractualizar(self, *args):
        self.eactid.set_text("")
        self.wactualizar.hide()
        return True

# VENTANA PARA EDITAR LOS CAMPOS DE UN REGISTRO

    # Accion que ocurre cuando clicamos "Actualizar" en la ventana de editar campos de un registro
    def clicksieditar(self, weditar):
        editid = self.ideditar
        nombre = self.enombre2.get_text()
        fecha = self.efecha2.get_text()
        lugar = self.elugar2.get_text()
        profesion = self.eprofesion2.get_text()
        aficiones = self.eaficiones2.get_text()
        # Comprueba que todo este en el formato adecuado; si lo esta, actualiza ese registro
        if len(nombre)==0 or len(lugar)==0 or len(profesion)==0 or len(aficiones)==0 or len(fecha)==0:
            self.werrtexto.show()
        elif not re.search("(19|20)\d{2}[-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])",fecha): 
            self.werrfecha.show()
        else:
            query= "UPDATE DatosFamilia SET Nombre = \"" + nombre + "\", FechaNacimiento = \""+ str(fecha) + "\", LugarResidencia = \"" + lugar + "\", Profesion = \"" + profesion +"\", Aficiones = \"" + aficiones + "\" WHERE id = " + str(editid) + ";"
            micursor.execute(query)
            conexion.commit()
            self.enombre2.set_text("")
            self.efecha2.set_text("")
            self.elugar2.set_text("")
            self.eprofesion2.set_text("")
            self.eaficiones2.set_text("")
            self.weditar.hide()

    # Cerrar la ventana editar
    def cerrareditar(self, *args):
        self.enombre2.set_text("")
        self.efecha2.set_text("")
        self.elugar2.set_text("")
        self.eprofesion2.set_text("")
        self.eaficiones2.set_text("")
        self.weditar.hide()
        return True

# VENTANA PARA BORRAR UNA ENTRADA

    # Accion que ocurre al clicar "Borrar" en la ventana general
    def clickborrar(self, wgeneral):
        self.wborrar.show()

    # Accion que ocurre al clicar "Borrar" en la ventana de borrar un registro
    def clicksiborrar(self, wborrar):
        borid = self.eborid.get_text()
        # Comprueba que la id introducida sea un digito
        if not re.search("\d+",borid):
            self.werrid.show()
        # Comprueba que sea una id existente y la borra
        else:
            borid = int(borid)
            query= "SELECT * FROM DatosFamilia WHERE 1;"
            micursor.execute(query)
            registros = micursor.fetchall()
            idok = 0
            for registro in registros:
                idok = idok + (registro["id"]==borid)
            if (idok==0):
                self.werrid.show()
            else:
                query= "DELETE FROM DatosFamilia WHERE id=" + str(borid) + ";"
                micursor.execute(query)
                conexion.commit()
                self.eborid.set_text("")
                self.wborrar.hide()

# Cerrar la ventana borrar
    def cerrarborrar(self, *args):
        self.eborid.set_text("")
        self.wborrar.hide()
        return True

# VENTANA ACERCA

    # Accion que ocurre al clicar "Acerca" en la ventana general
    def clickacerca(self, wgeneral):
        self.wacerca.show()

    # Cerrar la ventana acerca
    def cerraracerca(self, *args):
        self.wacerca.hide()        
        return True

# VENTANA ERROR DE TEXTO

    # Accion que ocurre al aceptar un mensaje de error de texto o cerrar su ventana
    def cerrarerrtexto(self, *args):
        self.werrtexto.hide()
        return True

# VENTANA ERROR DE FECHA

    # Accion que ocurre al aceptar un mensaje de error de fecha o cerrar su ventana
    def cerrarerrfecha(self, *args):
        self.werrfecha.hide()
        return True

# VENTANA ERROR DE ID

    # Accion que ocurre al aceptar un mensaje de error de id o cerrar su ventana
    def cerrarerrid(self, *args):
        self.werrid.hide()        
        return True


# MAIN

def main():
    window = Handler()
    Gtk.main()
    return 0

if __name__ == "__main__":
    main()
