from aplicacion import SMS, Mail, Configuracion, AppStore, Telefono
from central import Central
import numpy as np


class Celular:
    def __init__(self, id:int, nombre:str, modelo:str, OS:str, RAM:int, almacenamiento:int, numero:int, prendido:bool, bloqueado:bool, contraseña: int, ocupado:bool, correo:str,wifi:bool, redMovil:bool):
        self.id=self.validarId(id)
        self.nombre=nombre
        self.modelo=modelo
        self.OS=OS
        self.RAM=RAM #En GB
        self.almacenamiento=almacenamiento #En GB, almacenamiento de fabrica
        self.almacenamientodisp= self.almacenamiento #En GB, almacenamiento disponible para aplicaciones no esenciales
        self.numero=numero
        self.prendido=prendido
        self.bloqueado=bloqueado
        self.contraseña=contraseña
        self.correo=correo # direccion de correo personal asociado al celular
        self.wifi=wifi
        self.redMovil=redMovil #
        self.registrado = False #el celular no esta registrado en un principio
        self.sms=SMS('SMS',True,1)
        self.mail=Mail('Mail',True,1)
        self.configuracion=Configuracion('Configuracion',True,1)
        self.appstore=AppStore('Appstore',True,1)
        self.telefono = Telefono('Telefono',True,1)
        self.aplicaciones={'SMS':self.sms, 'Mail':self.mail, 'Configuracion':self.configuracion, 'Appstore':self.appstore,'Telefono': self.telefono} # Todas las aplicaciones del celular
        self.central=central1
        

        

    # Numero propio es el numero de la persona usando el celular
    def menu(self): #Este menú es del celular, las opciones que vería uno al interactuar con un celular, no el menú que nos permite seleccionar qué celular usar y esas cosas, eso es la clase Menu
        self.prendido = True #Esto es para asegurarse de que el valor se encuntre prendido, ya que puede estar apagado al instanciarse
        self.numero_origen=numero

        while self.prendido and self.desbloqueado:
            print("\n--- Aplicaciones ---")
            print("1. Mensajes")
            print("2. Recibir mensaje")
            print("3. Llamar por teléfono")
            print("4. Ver historial de llamadas")
            print("5. Ver chats")
            print("6. Apagar")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.sms.menuSMS(self,self.central,self.numero)
                
            elif opcion == "2":
                pass

            elif opcion == "3":
                numero = input("Ingresa el número al que deseas llamar: ")

            elif opcion == "4":
                print("\n--- Historial de Llamadas ---")

            elif opcion == "5":
                print("\n--- Chats ---")
            
            elif opcion == "6":
                print("Apagando dispositivo.")
                self.prenderApagar()

            else:
                print("Opción no válida. Inténtalo de nuevo.")

        else:
            print("Dispositivo apagado")
            input("Presione Enter para prender el dispositivo:")
            self.prenderApagar()
            clave = input("Ingrese la contraseña para desbloquear el dispositivo: ")
            while self.desbloquear(clave) == False:
                clave = input("Ingrese la contraseña para desbloquear el dispositivo: ")
            print("Dispositivo desbloqueado")
            self.menu()


    def validarId(id):
        if id not in Celular.ids:
            Celular.ids.add(id)
            return id
        else: raise ValueError('ya existe el id')

    def registrar(self):
        self.registrado = True

    def prenderApagar(self): #un mismoo boton prende y apaga el celular
        if self.prendido: #Si está prendido se apaga
            self.prendido = False
        else: #Si está apagado se prende
            self.prendido = True
            self.bloquear() #despues de prender el celular hay que reingresar la contraseña
            self.ocupado = False

            #cuando se prenda debe activarse la red movil
            if self.registrado == True:
                self.redMovil = True

            #preguntar SI DAR UN CELULAR DE BAJA ELIMINA LA INSTANCIA    
    
    def desbloquear(self, pass_given):
        if self.bloqueado:
            if pass_given==self.contraseña:
                self.bloqueado=False
                return True #Retorna true o flase para el momento de implementarlo en el menú
            else:
                print("Contraseña incorrecta, vuelve a intentarlo")
                return False
        else:
            raise Exception('El telefono ya estaba desbloqueado')
            
    def bloquear(self):
        self.bloqueado=True
    
    def verificarPrendido(self): #es necesario saber si esta prendido para recibir llamadas 
        return self.prendido
    
    def verificarOcupado(self): #verificar si esta prendido y si no esta en llamada
        if self.prendido:
            return self.ocupado
    
    def verificarWifi(self): 
        if self.prendido:
            return self.wifi

    def verificarRedmovil(self): 
        if self.prendido:
            return self.redMovil
    
    def verificarRegistrado(self):
        return self.registrado

    def instalarAplicacion(self,aplicacion): #falta incluir en el menu
        if aplicacion not in self.aplicaciones:
            if aplicacion.espacio < self.almacenamientodisp:
                self.aplicaciones.update(aplicacion.nombre, aplicacion)
                self.almacenamientodisp -= aplicacion.espacio
            else:
                print('no hay espacio disponible. intente desinstalar algunas aplicaciones')
        else:
            raise ValueError('La aplicacion ya esta instalada')

    def desinstalarAplicacion(self,aplicacion):
        if aplicacion in self.aplicaciones:
            if not aplicacion.esencial:
                self.aplicaciones.pop(aplicacion.nombre)
                self.almacenamientodisp += aplicacion.espacio
            else: raise ValueError('no se puede desinstalar una aplicacion esencial')
        else:
            raise ValueError('La aplicacion no esta instalada') 
    
    def __str__(self):
        return f'{self.nombre}, {self.id}'

    def __eq__(self, value):
        return self.id == value.id

central1=Central()



