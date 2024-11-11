from celular import *
import csv
from collections import deque
from central import *
import time
class Aplicacion:
    def __init__(self, central, nombre:str, espacio:int, abierto:bool):
        self.nombre=nombre
        #Las aplicaciones escenciales no se pueden eliminar
        self.espacio=espacio
        self.abierto = abierto
        self.central = central
        

    def abrirApp(self):
        if not self.abierto:
            self.abierto = True
            print(f"Aplicacion {self.nombre} abierta.")
        else:
            raise ValueError("La aplicacion ya esta abierta")

    def cerrarApp(self): 
        if self.abierto:
            self.abierto = False
            print(f"Aplicacion {self.nombre} cerrada.")
        else:
            raise ValueError('La aplicacion ya esta cerrada')
        

class Telefono(Aplicacion):
    def __init__(self, central, nombre: str, escencial: bool, espacio: int, abierto: bool,numero:int):
        super().__init__(central,nombre, espacio, abierto)
        self.ocupado = False
        self.numero = numero
        self.central = central
        self.historial = deque()

    def llamar(self,numeroDestino):
        if self.ocupado == False:
            if self.central.verificarRegistro(numeroDestino):
                self.ocupado = True
                inicio = time.time() 
                input("Cuando quiera terminar la llamada oprima Enter:")
                final = time.time()
                tiempoTranscurrido = final - inicio
                print(f'tiempo transcurrido en llamada {tiempoTranscurrido}')
                self.central.gestionarLlamada(self.numero,numeroDestino,tiempoTranscurrido)
                self.historial.append((self.numero,numeroDestino,tiempoTranscurrido))
                self.cortar()
            else:print('El telefono al que intenta llamar no esta registrado')
        else:
            raise ValueError('Este telefono no esta registrado')
    
    def verificarDisponibilidad(self):
        if self.ocupado == False:
            return True
    
    def cortar(self):
        self.ocupado = False
    
    def verLlamadas(self):
        self.historial = self.central.leerLlamadas(self.numero)
        self.historialCopia = self.bandeja.copy()
        while self.historialCopia:
            tupla = self.historialCopia.pop()
            numeroOrigen = tupla[0]
            numeroDestino = tupla[1]
            duracion = tupla[2]
            if numeroOrigen == self.numero:
                print(f'realizaste una llamada al numero{numeroDestino} con duracion {duracion}')
            else:
                print(f'recibiste una llamada del numero {numeroDestino} con duracion{duracion}')

    def menuLlamadas(self, central):
        self.abrirApp()
        continuar = True
        while continuar:
            print("\n--- Menu de Telefono ---")
            print("1. Realizar llamada")
            print('2. Ver historial de llamadas')
            print("3. Volver")
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                intentar_llamar = True
                while intentar_llamar:
                    print('Ingrese un numero telefonico para llamar, o escriba "cancelar" para volver al menu anterior')
                    numeroDestino = input()
                    try:
                        self.llamar(numeroDestino)
                    except ValueError as e:
                        print(e)
            elif opcion == '2':
                self.verLlamadas()
                pass
            elif opcion == "3":
                continuar = False
                self.cerrarApp()
            else:
                print("Opcion invalida. Intente de nuevo.")


# DiccionarioChats guarda en clave otros celulares y en value una tupla compuesta por (Quien mando el mensaje, mensaje)
class SMS(Aplicacion): 
    def __init__(self, central, nombre: str, escencial: bool, espacio: int, abierto: bool,numero:int):
        super().__init__(central, nombre, espacio, abierto)
        self.escencial = escencial
        self.chats=dict() #Diccionario de clave numero, valor pila (bandeja de entrada que contiene tuplas) 
        self.nombre = 'SMS'
        self.numero = numero
        self.central = central
    
    def menuSMS(self):
        continuar=True
        self.abrirApp()
    
        while continuar==True:
            print("1. Mandar mensaje")
            print("2. Ver chats")
            print("3. Volver al menu anterior")

            opcion = input("Elige una opcion: ")

            if opcion== "1":
                numero_destino = input("Ingresa el numero de telefono: ")
                mensaje = input("Escribe el mensaje: ")
                self.enviarMensaje(self.numero,numero_destino,mensaje,self.central)
                
                
            if opcion== "2":
                self.verChats()
                
            if opcion== "3":
                continuar=False
                print("Has salido de mensajes")
                self.cerrarApp()
        #            self.central.verificarRegistroMensajes(celular_origen,numero_origen,numero_destino,mensaje)

    def enviarMensaje(self,numeroOrigen,numeroDestino,mensaje):
        if not numeroOrigen:
            numeroValido = False
            while not numeroValido:
                try:
                    numeroOrigen = int(input('Ingrese un numero de celular'))
                    numeroValido = True
                except ValueError('Ingrese un numero correcto, solo digitos del 0-9 y llame al 11') as e:
                    print(e)
                else:
                    if numeroDestino != 11:
                        numeroValido = False
                        print('Debe registrar su dispositivo enviando un mensaje al 11')
        elif numeroDestino not in self.chats:
            self.bandeja = deque()
            self.bandeja.append((str(numeroOrigen),str(numeroDestino),mensaje))
            self.chats[numeroDestino]= self.bandeja
            self.central.gestionarSms(numeroOrigen,numeroDestino,mensaje)
        else:
            self.chats.get(numeroDestino).append((str(numeroOrigen),str(numeroDestino),mensaje))
            self.central.gestionarSms(numeroOrigen,numeroDestino,numeroDestino,mensaje)
        print(self.chats)
    
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
    def __init__(self, central, nombre: str, escencial: bool, espacio: int, abierto: bool, direccion: str):
        super().__init__(central, nombre, espacio, abierto)
        self.nombre = 'Mail'
        self.lista_mails = []
        self.direccion = direccion
        self.recibidos_no_leidos = []
        self.recibidos_leidos =[]
        self.recibidos = []
        self.central = central

    # def visualizar_mails_leidos(self):
    #     try:
    #         with open("mails.csv","r",newline="") as file:
    #             reader = csv.reader(file)
    #             for line in reader:
    #                 if line[1] == self.direccion:
    #                     if eval(line[5]) == False:
    #                         self.recibidos_no_leidos.insert(0,(line[0],line[2],line[3],line[4],line[5]))
    #                     else:
    #                         self.recibidos_leidos.insert(0,(line[0],line[2],line[3],line[4],line[5]))
    #     except Exception as e:
    #         print(e)
                
    # def visualizar_mails_tiempo(self):
    #     try:
    #         with open("mails.csv","r",newline="") as file:
    #             reader = csv.reader(file)
    #             for line in reader:
    #                 if line[1] == self.direccion:
    #                     self.recibidos.insert(0,(line[0],line[2],line[3],line[4],line[5]))
    #     except Exception as e:
    #         print(e)

    def redactar_mail(self,central):
        self.destinatario = input("Ingrese la direccion del destinatario: ")
        self.titulo = input("Ingrese el titulo del mensaje: ")
        self.mensaje = input("Redacte el contenido del mensaje: ")
        opcion_invalida = True
        while opcion_invalida:
            opcion = input("El mail es urgente? (Y/N): ")
            if opcion.lower == "y":
                self.escencial = True
                opcion_invalida = False
            elif opcion.lower == "n":
                self.escencial = False
                opcion_invalida = False
            else:
                print("Opcion invalida")
            self.abierto = False
            self.central.gestionarMail(self.direccion,self.destinatario,self.titulo,self.mensaje,self.escencial,self.abierto)

    def menuMail(self, central):
        self.abrirApp()
        continuar = True
        while continuar:
            print("\n--- Menu de Mail ---")
            print("1. Redactar mensaje")
            print("2. Ver tablero de entrada")
            print("3. Volver al menu anterior")
            nav = input("Elija una opciun: ")
            if nav == "1":
                self.redactar_mail(central)
            elif nav == "2":
                print("Ver mensajes segun: \n1. No leidos primero\n2. Por fecha")
                opcion = input("Elija una opcion: ")
                if opcion == "1":
                    self.recibidos_no_leidos, self.recibidos_leidos = self.central.visualizar_mails_leidos()
                    for i in self.recibidos_no_leidos:
                        print(i)
                    for i in self.recibidos_leidos:
                        print(i)
                elif opcion == "2":
                    self.recibidos = self.central.visualizar_mails_tiempo()
                    for i in self.recibidos:
                        print(i)
                else:
                    print("Opcion invalida")
            elif nav == "3":
                continuar = False
            else:
                print("Opcion invalida")

        
class Contacto(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, escencial, espacio, abierto)
        self.contactos={}
        self.nombre = 'Contacto'

# Agenda un contacto guardandolo en un diccionario mediante el numero y el nombre
    def agendarContacto(self,celular,numero,nombre):
        if self.central.dispositivoRegistrado(numero):
            if numero not in self.contactos.get:
                self.contactos[celular].append((numero,nombre))
                self.central.agregarContacto()
            else:
                print('No se puede agendar ese numero porque ya esta agendado, pruebe actualizando el contacto')

# Actualiza el contacto y nombre en el diccionario
    def actualizarContacto(self,celular,numero,nombre):
        if numero not in self.contactos[celular]:
            print("Ese numero no existe, intente agendarlo")
        else:
            self.contactos[celular].append((numero,nombre))

# Elimina el contacto de diccionario
    def eliminarContacto(self,numero,celular):
        if numero not in self.contactos.keys():
            raise ValueError('Este numero no esta agendado')
        else:
            self.contactos[celular].remove(numero)

    def menuContacto(self,celular):
        self.abrirApp()
        continuar = True
        while continuar:
            print("\n----Menu de Contacto---")
            print("1. Agendar contacto")
            print("2. Actualizar contacto")
            print("3. Eliminar contacto")
            print("4. Volver al menu anterior")
            nav = input("Elige una opcion: ")
            if nav == "1":
                self.agendarContacto(celular,input("Ingrese el numero del contacto: "), input("Ingrese el nombre del contacto: "))
            elif nav == "2":
                self.actualizarContacto(celular,input("Ingrese el numero del contacto: "), input("Ingrese el nuevo nombre del contacto: "))
            elif nav == "3":
                self.eliminarContacto(celular,input("Ingrese el numero del contacto: "))
            elif nav == "4":
                continuar = False
                try:
                    with open('contactos.csv','a',newline='') as archivo:
                        escritor=csv.writer(archivo)
                        for celular,numero in self.contactos:
                            escritor.writerow([celular,numero])
                except FileNotFoundError:
                    with open('contactos.csv','w',newline='') as archivo:
                        escritor=csv.writer(archivo)
                        escritor.writerow(["Celular","Numero agendado","Nombre"])
                        escritor.writerow([celular,numero])
                self.cerrarApp()
            else:
                print("Opcion invalida")

class Configuracion(Aplicacion):
    def __init__(self, central:object, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, central, espacio, abierto)
        self.nombre = 'Configuracion'

    def cambiarNombreTelefono(self,celular):
        try:
            nuevo_nombre = input("Ingrese el nuevo nombre del dispositivo: ")
            if nuevo_nombre.strip():  # Verifica que no este vacio
                celular.nombre = nuevo_nombre
                print(f"Nombre cambiado exitosamente a: {nuevo_nombre}")
            else:
                print("Error: El nombre no puede estar vacio")
        except Exception as e:
            print(f"Error al cambiar el nombre: {e}")

    def cambiarCodigoDesbloqueo(self,celular):
        try:
            codigo_actual = input("Ingrese el codigo actual: ")
            if codigo_actual == celular.contrasenia:
                nuevo_codigo = input("Ingrese el nuevo codigo: ")
                celular.contrasenia = nuevo_codigo
                print("Codigo cambiado exitosamente")
            else:
                print("Error: Codigo actual incorrecto")
        except ValueError:
            print("Error: El codigo debe ser un numero")

    def activarRedMovil(self, celular, central):
        if central.verificar_registro(celular.id):
            if not celular.redMovil:
                celular.redMovil = True
                print("Red movil activada")
        else:
            print("La red movil ya esta activa")
            
    def desactivarRedMovil(self, celular, central):
        if central.verificar_registro(self.id):
            if celular.redMovil:
                celular.redMovil = False
                print("Red movil desactivada")
        else:
            print("La red movil ya esta desactivada")
 
    def activarWifi(self,celular):
        if not celular.wifi:
            celular.wifi = True
            print("WiFi activado")
        else:
            print("El WiFi ya esta activo")
   
    def desactivarWifi(self,celular):
        if celular.wifi:
                celular.wifi = False
                print("WiFi desactivado")
        else:
                print("El WiFi ya esta desactivado")


    def menuConfig(self,celular):
        continuar = True
        self.abrirApp()
        while continuar:
            print("\n----Menu de Configuracion---")
            print("1. Cambiar nombre del telefono")
            print("2. Cambiar codigo de desbloqueo")
            print("3. Activar la red movil")
            print("4. Desactivar la red movil")
            print("5. Activar Wifi")
            print("6. Desactivar Wifi")
            print("7. Volver al menu anterior")

            command = input("Elige una opcion: ")
            if command == "1":
                self.cambiarNombreTelefono(celular)
            elif command == "2":
                self.cambiarCodigoDesbloqueo(celular)
            elif command == "3":
                if celular.redMovil==True:
                    print("La red movil ya esta activada")
                else:
                    self.activarRedMovil(celular)
            elif command == "4":
                if celular.redMovil==True:
                    self.desactivarRedMovil(celular)
                else:
                    print("La red movil ya esta desactivada")
            elif command == "5":
                if celular.wifi==True:
                    print("El wifi ya esta activado")
                else:
                    self.activarWifi(celular)
            elif command == "6":
                if celular.wifi==True:
                    self.desactivarWifi(celular)
                else:
                    print("El wifi ya esta desactivado")
            elif command == "7":
                continuar = False
                self.cerrarApp()
            else:print("Opcion invalida")
        

class AppStore(Aplicacion):
    def __init__(self, central, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, central, espacio, abierto)
        self.escencial=escencial
        
    def descargarAplicacion(self,celular,app):
        if app not in celular.aplicaciones:
            celular.aplicaciones.add(app)
        else:
            print("Esta aplicacion ya esta descargada")

    def menuApp(self, celular):
        continuar = True
        self.abrirApp()
        while continuar:
            print("\n----Menu de Appstore---")
            print("1. Descargar aplicacion")
            print("2. Volver al menu anterior")
            nav = input()
            if nav == "1":
                self.descargarAplicacion(celular, input("Ingrese una aplicacion para descargar: "))
            elif nav == "2":
                continuar = False
                self.cerrarApp()
            else:
                print("Opcion invalida")
                



#pivote
#diccionario={1:celular1,2:celular2}
#for celular in diccionario.values()
