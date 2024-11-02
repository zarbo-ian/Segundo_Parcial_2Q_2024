from celular import *
import csv
from collections import deque
class Aplicacion:
    def __init__(self, nombre:str, escencial:bool, espacio:int, abierto:bool,instalada:bool):
        self.nombre=nombre
        #Los escenciales no se pueden eliminar
        self.escencial=escencial
        self.espacio=espacio
        self.abierto = False
        self.instalada = instalada

    def abrirApp(self):
        if not self.abierto:
            self.abierto = True
            print(f"Aplicación {self.nombre} abierta.")
        else:
            raise ValueError("La aplicacion ya esta abierta")

    def cerrarApp(self): 
        if self.abierta:
            self.abierta = False
            print(f"Aplicación {self.nombre} cerrada.")
        else:
            raise ValueError('La aplicacion ya esta cerrada')
        

class Telefono(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, escencial, espacio, abierto)
        self.ocupado = False
    
    def llamar(self,otroTelefono):
        if self.ocupado == False:
            if otroTelefono.ocupado == False:
                self.ocupado = True    
                input("Cuando quiera terminar la llamada oprima Enter:")
                self.ocupado = False
                otroTelefono.ocupado = False
            else:print('Este telefono no esta disponible')
        else:
            raise ValueError('El telefono ya esta llamada')
    
    def recibirLlamada(self, otroTelefono):
        self.ocupado = True
    
    def cortar(self, otroTelefono):
        self.ocupado = False

    def menuLlamadas(self, central):
        continuar = True
        while continuar:
            print("\n--- Menú de Telefono ---")
            print("1. Realizar llamada")
            print("2. Volver")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                intentar_llamar = True
                while intentar_llamar:
                    print('Ingrese un número telefónico para llamar, o escriba "cancelar" para volver al menú anterior')
                    numero = input()
                    if central.dispositivos_registrados.get(numero) != None:
                        try:
                            self.llamar(numero)
                        except ValueError as e:
                            print(e)
                    elif numero.lower == "cancelar":
                        intentar_llamar = False
                    else:
                        print("Numero no existe, intentelo de nuevo")
            elif opcion == "2":
                continuar = False
            else:
                print("Opción inválida. Intente de nuevo.")

# DiccionarioChats guarda en clave otros celulares y en value una tupla compuesta por (Quien mando el mensaje, mensaje)
class SMS(Aplicacion): 
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool,ocupado:bool,id:int,numero:int):
        super().__init__(nombre, escencial, espacio, abierto)
        self.diccionarioChats={} #DEBERIA SER UNA PILA CON TUPLAS (NUMERO,MENSAJE)
        self.nombre = 'SMS'
        self.id = id
        self.numero = numero
    
    def menuSMS(self,numero_origen,central): #pasarle los datos necesarios telefono remitente etc
        continuar=True
        self.abrirApp()
        self.bajarChats()
        while self.prendido and self.bloqueado:
            while continuar==True:
                print("1. Mandar mensaje")
                print("2. Ver chats")
                print("3. Volver al menú anterior")

                opcion = input("Elige una opción: ")

                if opcion== "1":
                    numero_destino = input("Ingresa el número de teléfono: ")
                    mensaje = input("Escribe el mensaje: ")
                    self.enviarMensaje(numero_destino,mensaje)
                    
                if opcion== "2":
                    self.verChats()
                    
                if opcion== "3":
                    continuar=False
                    print("Has salido de mensajes")
                    self.cerrarApp()
                    self.cargarChats()
            #            self.central.verificarRegistroMensajes(celular_origen,numero_origen,numero_destino,mensaje)

    def enviarMensaje(self,idOrigen,numeroOrigen,numeroDestino,mensaje,central): #debe ser una pila
        if numeroOrigen not in self.diccionarioChats.keys():
            self.diccionarioChats[numeroOrigen] = deque()
            self.diccionarioChats.get(numeroOrigen).append((numeroOrigen,mensaje))
            central.gestionarSms(numeroOrigen)
        else:
            self.diccionarioChats.get(numeroOrigen).append((numeroOrigen,mensaje))
        print(self.diccionarioChats)

    # def recibirMensaje(self,numero_remitente,numero_destinatario,mensaje):
    #     if numero_remitente not in self.diccionarioChats:
    #         self.diccionarioChats[numero_remitente] = [(numero_remitente,mensaje)]
    #     else:
    #         self.diccionarioChats.get(numero_remitente).append((numero_remitente,mensaje))
    #     print(self.diccionarioChats)

    def bajarChats(self): #carga automatica de el csv
        #with open csv:
        #leer todas las lineas que empiezen con el self.id
        #for line in csv:
        #    if line empieza con self.id
        pass
    
    def cargarChats(self):    
        try:
            with open('chats', mode='a', newline='') as file:
                writer = csv.writer(file)
                # Encabezado si el archivo es nuevo
                if file.tell() == 0:
                    writer.writerow(["ID", "Nombre", "Modelo", "OS", "RAM", "Almacenamiento", "Numero", "Prendido", "Bloqueado", "Contraseña", "Correo", "WiFi", "RedMovil"])
        except Exception:
            pass
    
    def verChats(self):
        pass


class Mail(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool, direccion: str):
        super().__init__(nombre, escencial, espacio, abierto)
        self.nombre = 'Mail'
    
    def enviar_mail(self, direccion):

class Contacto(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, escencial, espacio, abierto)
        self.diccionario={}
        self.nombre = 'Contacto'

# Agenda un contacto guardandolo en un diccionario mediante el numero y el nombre
    def agendarContacto(self,numero,nombre):
        if numero not in self.diccionario.keys():
            self.diccionario[numero]=nombre
        else:
            print('No se puede agendar ese numero porque ya esta agendado, pruebe actualizando el contacto')

# Actualiza el contacto y nombre en el diccionario
    def actualizarContacto(self,numero,nombre):
        if numero not in self.diccionario.keys():
            print("Ese numero no existe, intente agendarlo")
        else:
            self.diccionario[numero]=nombre

# Elimina el contacto de diccionario
    def eliminarContacto(self,numero):
        if numero not in self.diccionario.keys():
            raise ValueError('Este numero no esta agendado')
        else:
            self.diccionario.pop(numero)

    def menuContacto(self):
        continuar = True
        while continuar:
            print("\n----Menú de Configuracion---")
            print("1. Agendar contacto")
            print("2. Actualizar contacto")
            print("3. Eliminar contacto")
            print("4. Volver al menú anterior")
            nav = input("Elige una opcion: ")
            if nav == "1":
                self.agendarContacto(input("Ingrese el número del contacto: "), input("Ingrese el nombre del contacto: "))
            elif nav == "2":
                self.actualizarContacto(input("Ingrese el número del contacto: "), input("Ingrese el nuevo nombre del contacto: "))
            elif nav == "3":
                self.eliminarContacto(input("Ingrese el numero del contacto: "))
            elif nav == "4":
                continuar = False
            else:
                print("Opción inválida")

class Configuracion(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, escencial, espacio, abierto)

    def activarRedMovil(self):
        self.redMovil = True #La red movil es un atributo del celular, por lo que cel es un objeto del tipo celular
    
    def desactivarRedMovil(self):
        self.redMovil = False     

    def nombreTelefono(self):
        nom = input("Ingrese el nombre del dispositivo: ")
        self.nombre = nom

    def codigoDesbloqueo(self):
        cod = input("Ingrese el nuevo codigo de desbloqueo: ")
        self.contraseña  = cod

    def accederWifi(self):
        self.wifi = True

    def desactivarWifi(self):
        self.wifi=False

    def menuConfig(self,cel):
        continuar = True
        while continuar:
            print("\n----Menú de Configuracion---")
            print("1. Cambiar nombre del telefono")
            print("2. Cambiar código de desbloqueo")
            print("3. Activar la red movil")
            print("4. Desactivar la red movil")
            print("5. Activar Wifi")
            print("6. Desactivar Wifi")
            print("7. Volver al menú anterior")

            command = input("Elige una opcion: ")
            if command == "1":
                self.nombreTelefono()
            elif command == "2":
                self.codigoDesbloqueo()
            elif command == "3":
                if self.redMovil:
                    print("La red movil ya está activada")
                else:
                    self.activarRedMovil()
            elif command == "4":
                if self.redMovil:
                    self.desactivarRedMovil()
                else:
                    print("La red movil ya está desactivada")
            elif command == "5":
                if self.wifi:
                    print("El wifi ya está activado")
                else:
                    self.accederWifi()
            elif command == "6":
                if self.wifi:
                    self.desactivarWifi()
                else:
                    print("El wifi ya está desactivado")
            elif command == "7":
                continuar = False
            else:print("Opción inválida")
        

class AppStore(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, escencial, espacio, abierto)
    def descargarAplicacion(self,celular,app):
        if app not in celular.aplicaciones:
            celular.aplicaciones.add(app)
        else:
            print("Esta aplicación ya está descargada")

    def menuApp(self, celular):
        continuar = True
        while continuar:
            print("\n----Menú de Appstore---")
            print("1. Descargar aplicacion")
            print("2. Volver al menú anterior")
            nav = input()
            if nav == "1":
                self.descargarAplicacion(celular, input("Ingrese una aplicación para descargar: "))
            elif nav == "2":
                continuar = False
            else:
                print("Opción inválida")
                

