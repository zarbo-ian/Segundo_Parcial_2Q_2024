from celular import *
import csv
from collections import deque
from central import *
class Aplicacion:
    def __init__(self, nombre:str, escencial:bool, espacio:int, abierto:bool):
        self.nombre=nombre
        #Los escenciales no se pueden eliminar
        self.escencial=escencial
        self.espacio=espacio
        self.abierto = False


    def abrirApp(self):
        if not self.abierto:
            self.abierto = True
            print(f"Aplicación {self.nombre} abierta.")
        else:
            raise ValueError("La aplicacion ya esta abierta")

    def cerrarApp(self): 
        if self.abierto:
            self.abierto = False
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
    def __init__(self,central, nombre: str, escencial: bool, espacio: int, abierto: bool,id:int,numero:int,ocupado:bool=None):
        super().__init__(nombre, escencial, espacio, abierto)
        self.escencial = escencial
        self.chats=dict() #DEBERIA SER UNA PILA CON TUPLAS (NUMERO,MENSAJE)
        self.nombre = 'SMS'
        self.id = id
        self.numero = numero
        self.central = central
    
    def menuSMS(self,celular): #pasarle los datos necesarios telefono remitente etc
        continuar=True
        self.abrirApp()
    
        while continuar==True:
            print("1. Mandar mensaje")
            print("2. Ver chats")
            print("3. Volver al menú anterior")

            opcion = input("Elige una opción: ")

            if opcion== "1":
                numero_destino = input("Ingresa el número de teléfono: ")
                mensaje = input("Escribe el mensaje: ")
                self.enviarMensaje(celular.id,self.numero,numero_destino,mensaje,self.central)
                
                
            if opcion== "2":
                self.verChats()
                
            if opcion== "3":
                continuar=False
                print("Has salido de mensajes")
                self.cerrarApp()
                self.cargarChats()
        #            self.central.verificarRegistroMensajes(celular_origen,numero_origen,numero_destino,mensaje)

    def enviarMensaje(self,numeroOrigen,numeroDestino,mensaje):
        
        if numeroDestino not in self.chats:
            self.bandeja = deque()
            self.bandeja.append((str(numeroOrigen),str(numeroDestino),mensaje))
            self.chats[numeroDestino]= self.bandeja
            self.central.gestionarSms(numeroOrigen,numeroDestino,mensaje)
        else:
            self.chats.get(numeroDestino).append((str(numeroOrigen),str(numeroDestino),mensaje))
            self.central.gestionarSms(numeroOrigen,numeroDestino,numeroDestino,mensaje)
        print(self.chats)
        

    #def bajarChats(self,central): #carga automatica de el csv al celular de sus mensajes por chat
        #self.chats = central.leerSms(self.numero)
        
            
    
    # def cargarChats(self):    
    #     try:
    #         with open('chats', mode='a', newline='') as file:
    #             writer = csv.writer(file)
    #             # Encabezado si el archivo es nuevo
    #             chatsCopia = self.chats.copy
    #             while chatsCopia:
    #                 elemento = self.chatsCopia.pop()
    #                 writer.writerow[str(self.id),str(elemento[1]),str(elemento[2]),str(elemento[3])]       
    #     except FileNotFoundError('No se encontro el archivo') as e:
    #         print(e)
    
    def verChats(self):
        self.chats = self.central.leerSms(self.numero)
        for contacto in self.chats:
            self.bandeja=self.chats.get(contacto)
            self.bandejaCopia = self.bandeja.copy()
            while self.bandejaCopia:
                print(self.bandejaCopia.pop())

        

# central1 = Central()
# smsprueba = SMS('SMS',True,50,True,50,50300,False)
# smsprueba.enviarMensaje(11234451,22236918660,119999999,'Hola',central1)
# smsprueba.bajarChats()
# print(smsprueba.chats)
class Mail(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool, direccion: str):
        super().__init__(nombre, escencial, espacio, abierto)
        self.nombre = 'Mail'
        self.lista_mails = []
        self.direccion = direccion
        self.recibidos_no_leidos = []
        self.recibidos_leidos =[]
        self.recibidos = []
    
    # def enviar_mail(self, direccion_origen, direccion_destino, mensaje):
    #     self.lista_mails.insert(0,mensaje)
    #     print(self.lista_mails)

    def visualizar_mails_leidos(self):
        try:
            with open("mails.csv","r",newline="") as file:
                reader = csv.reader(file)
                for line in reader:
                    if line[1] == self.direccion:
                        if eval(line[5]) == False:
                            self.recibidos_no_leidos.insert(0,(line[0],line[2],line[3],line[4],line[5]))
                        else:
                            self.recibidos_leidos.insert(0,(line[0],line[2],line[3],line[4],line[5]))
                    else:
                        self.recibidos.insert(0,(line[0],line[2],line[3],line[4],line[5]))

        except Exception as e:
            print(e)
                

    def redactar_mail(self,central):
        self.destinatario = input("Ingrese la direccion del destinatario: ")
        self.titulo = input("Ingrese el titulo del mensaje: ")
        self.mensaje = input("Redacte el contenido del mensaje: ")
        opcion_invalida = True
        while opcion_invalida:
            opcion = input("¿El mail es urgente? (Y/N): ")
            if opcion.lower == "y":
                self.escencial = True
                opcion_invalida = False
            elif opcion.lower == "n":
                self.escencial = False
                opcion_invalida = False
            else:
                print("Opcion invalida")
            self.abierto = False
            central.gesttionarMail(self.direccion,self.destinatario,self.titulo,self.mensaje,self.escencial,self.abierto)

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
                self.redactar_mail(central)
            elif nav == "2":
                print("Ver mensajes según: \n1. No leídos primero\n2. Por fecha")
                opcion = input("Elija una opcion: ")
                if opcion == "1":
                    for i in self.recibidos_no_leidos:
                        print(i)
                    for i in self.recibidos_leidos:
                        print(i)
                elif opcion == "2":
                    for i in self.recibidos:
                        print(i)
                else:
                    print("Opcion inválida")

        
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
            print("\n----Menú de Contacto---")
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

    def cambiarNombreTelefono(self,celular):
        try:
            nuevo_nombre = input("Ingrese el nuevo nombre del dispositivo: ")
            if nuevo_nombre.strip():  # Verifica que no esté vacío
                celular.nombre = nuevo_nombre
                filas=[]
                with open('celulares.csv','r',newline='') as archivo:
                    lector=csv.reader(archivo)
                    for i in lector:
                        if i[0]==celular.id:
                            i[1]=nuevo_nombre
                        filas.append(i)
                with open('celulares.csv','w',newline='') as archivo:
                    escritor=csv.writer(archivo)
                    escritor.writerows(filas)

                print(f"Nombre cambiado exitosamente a: {nuevo_nombre}")
            else:
                print("Error: El nombre no puede estar vacío")
        except Exception as e:
            print(f"Error al cambiar el nombre: {e}")

    def cambiarCodigoDesbloqueo(self,celular):
        try:
            codigo_actual = input("Ingrese el código actual: ")
            if codigo_actual == celular.contraseña:
                nuevo_codigo = input("Ingrese el nuevo código: ")
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
        if central.verificar_registro(self.id):
            if celular.redMovil:
                celular.redMovil = False
                print("Red móvil desactivada")
        else:
            print("La red móvil ya está desactivada")
 
    def activarWifi(self,celular):
        if not celular.wifi:
            celular.wifi = True
            print("WiFi activado")
        else:
            print("El WiFi ya está activo")
   
    def desactivarWifi(self,celular):
        if celular.wifi:
                celular.wifi = False
                print("WiFi desactivado")
        else:
                print("El WiFi ya está desactivado")


    def menuConfig(self,celular):
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
                self.cambiarNombreTelefono(celular)
            elif command == "2":
                self.codigoDesbloqueo(celular)
            elif command == "3":
                if celular.redMovil:
                    print("La red movil ya está activada")
                else:
                    self.activarRedMovil(celular)
            elif command == "4":
                if celular.redMovil:
                    self.desactivarRedMovil(celular)
                else:
                    print("La red movil ya está desactivada")
            elif command == "5":
                if celular.wifi:
                    print("El wifi ya está activado")
                else:
                    self.activarWifi(celular)
            elif command == "6":
                if celular.wifi:
                    self.desactivarWifi(celular)
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
                



#pivote
#diccionario={1:celular1,2:celular2}
#for celular in diccionario.values()
