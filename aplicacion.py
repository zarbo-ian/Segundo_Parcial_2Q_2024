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
        self.abrirApp()
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
                self.cerrarApp()
            else:
                print("Opción inválida. Intente de nuevo.")

# DiccionarioChats guarda en clave otros celulares y en value una tupla compuesta por (Quien mando el mensaje, mensaje)
class SMS(Aplicacion): 
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool,ocupado:bool,id:int,numero:int):
        super().__init__(nombre, escencial, espacio, abierto)
        self.escencial = escencial
        self.chats=deque() #DEBERIA SER UNA PILA CON TUPLAS (NUMERO,MENSAJE)
        self.nombre = 'SMS'
        self.id = id
        self.numero = numero
    
    def menuSMS(self,numero_origen,central): #pasarle los datos necesarios telefono remitente etc
        continuar=True
        self.abrirApp()
        self.bajarChats()
    
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

    def enviarMensaje(self,idOrigen,numeroOrigen,idDestino,numeroDestino,mensaje,central): #debe ser una pila
        if numeroDestino not in self.chats:
            bandeja = deque
            self.bandeja.append(idOrigen,idDestino,mensaje)
            self.chats.append(bandeja)

            central.gestionarSms(numeroOrigen,idOrigen,numeroDestino,idDestino,mensaje)
        else:
            central.gestionarSms(numeroOrigen,idOrigen,numeroDestino,idDestino,mensaje)
        print(self.chats)

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
        #    if line[0] = str(self.id):
                #

        pass
    
    def cargarChats(self):    
        try:
            with open('chats', mode='a', newline='') as file:
                writer = csv.writer(file)
                # Encabezado si el archivo es nuevo
                chatsCopia = self.chats.copy
                while chatsCopia:
                    elemento = self.chatsCopia.pop()
                    writer.writerow[str(self.id),str(elemento[1]),str(elemento[2]),str(elemento[3])]       
        except FileNotFoundError('No se encontro el archivo') as e:
            print(e)
    
    def verChats(self):
        pass

class Mail(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool, direccion: str):
        super().__init__(nombre, escencial, espacio, abierto)
        self.nombre = 'Mail'
        self.lista_mails = []
        self.direccion = direccion
    
    def enviar_mail(self, direccion_origen, direccion_destino, mensaje):
        self.lista_mails.insert(0,mensaje)
        print(self.lista_mails)

    def redactar_mail(self):
        self.destinatario = input("Ingrese la direccion del destinatario: ")
        self.titulo = input("Ingrese el titulo del mensaje: ")
        self.mensaje = input("Redacte el contenido del mensaje: ")
        opcion_invalida = True
        while opcion_invalida:
            opcion = input("¿El mail es escencial? (Y/N): ")
            if opcion.lower == "y":
                self.escencial = True
                opcion_invalida = False
            elif opcion.lower == "n":
                self.escencial = False
                opcion_invalida = False
            else:
                print("Opcion invalida")

    def menuMail(self, central):
        self.abrirApp()
        continuar = True
        while continuar:
            print("\n--- Menú de Mail ---")
            print("1. Redactar mensaje")
            print("2. Ver tablero de entrada")
            print("3. Volver al menú anterior")
            nav = input("Elija una opción: ")
            if nav == "1":
                self.redactar_mail()
            elif nav == "2":
                print("Ver mensajes según: \n1. No leídos primero\n2. Por fecha")

        
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
        self.abrirApp()
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
                self.cerrarApp()
            else:
                print("Opción inválida")

class Configuracion(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, escencial, espacio, abierto)
        self.nombre = 'Configuracion'

    def cambiarNombreTelefono(self, celular):
        try:
            nuevo_nombre = input("Ingrese el nuevo nombre del dispositivo: ")
            if nuevo_nombre.strip():  # Verifica que no esté vacío
                celular.nombre = nuevo_nombre
                print(f"Nombre cambiado exitosamente a: {nuevo_nombre}")
            else:
                print("Error: El nombre no puede estar vacío")
        except Exception as e:
            print(f"Error al cambiar el nombre: {e}")

    def cambiarCodigoDesbloqueo(self, celular):
        try:
            codigo_actual = int(input("Ingrese el código actual: "))
            if codigo_actual == celular.contraseña:
                nuevo_codigo = int(input("Ingrese el nuevo código: "))
                celular.contraseña = nuevo_codigo
                print("Código cambiado exitosamente")
            else:
                print("Error: Código actual incorrecto")
        except ValueError:
            print("Error: El código debe ser un número")

    def activarRedMovil(self, celular, central):
        if central.verificar_registro(celular.id):
            if not celular.redMovil:
                celular.redMovil = True
                print("Red móvil activada")
        else:
            print("La red móvil ya está activa")
            
    def desactivaRrRedMovil(self, celular, central):
        if central.verificar_registro(celular.id):
            if celular.redMovil:
                celular.redMovil = False
                print("Red móvil desactivada")
        else:
            print("La red móvil ya está desactivada")
 
    def activarWifi(self, celular):
        if not celular.wifi:
            celular.wifi = True
            print("WiFi activado")
        else:
            print("El WiFi ya está activo")
   
    def desactivarWifi(self, celular):
        if celular.wifi:
                celular.wifi = False
                print("WiFi desactivado")
        else:
                print("El WiFi ya está desactivado")


    def menuConfig(self,cel):
        continuar = True
        self.abrirApp()
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
                self.cerrarApp()
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
        self.abrirApp()
        while continuar:
            print("\n----Menú de Appstore---")
            print("1. Descargar aplicacion")
            print("2. Volver al menú anterior")
            nav = input()
            if nav == "1":
                self.descargarAplicacion(celular, input("Ingrese una aplicación para descargar: "))
            elif nav == "2":
                continuar = False
                self.cerrarApp()
            else:
                print("Opción inválida")
                

