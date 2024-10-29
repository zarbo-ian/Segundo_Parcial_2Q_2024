from aplicacion import SMS, Mail, Configuracion, AppStore, Telefono
#from central import Central   self.id=self.validarId(id)
import numpy as np
import csv
from tpEDP import Interfaz


class Celular:
    ids=set()
    interfaz = Interfaz()
    def __init__(self, id:int, nombre:str, modelo:str, OS:str, RAM:int, almacenamiento:int, numero:int, prendido:bool, bloqueado:bool, contraseña: int, correo:str,wifi:bool, redMovil:bool, ocupado:bool=False, chatMensajes:list = None):
        self.id=id
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
        #self.registrado = False #el celular no esta registrado en un principio
        self.chatMensajes={}

# Necesito que esten asi para probar cosas y que no salte error
    #    self.sms=SMS('SMS',True,1)
    #    self.mail=Mail('Mail',True,1)
    #    self.configuracion=Configuracion('Configuracion',True,1)
    #    self.appstore=AppStore('Appstore',True,1)
    #    self.telefono = Telefono('Telefono',True,1)
    #    self.aplicaciones={'SMS':self.sms, 'Mail':self.mail, 'Configuracion':self.configuracion, 'Appstore':self.appstore,'Telefono': self.telefono} # Todas las aplicaciones del celular
       # self.central=central1 # Como hacemos que todos tengan la misma central??
        

    def guardar_en_csv(self):
        # Definir el nombre del archivo CSV
        archivo_csv = "celulares.csv"
        
        # Verificar si el archivo existe para agregar encabezados solo si es nuevo
        try:
            with open(archivo_csv, mode='a', newline='') as file:
                writer = csv.writer(file)
                # Encabezado si el archivo es nuevo
                if file.tell() == 0:
                    writer.writerow(["ID", "Nombre", "Modelo", "OS", "RAM", "Almacenamiento", "Numero", "Prendido", "Bloqueado", "Contraseña", "Correo", "WiFi", "RedMovil"])
                
                # Escribir los datos del celular
                writer.writerow([
                    self.id, self.nombre, self.modelo, self.OS, self.RAM, self.almacenamiento,
                    self.numero, self.prendido, self.bloqueado, self.contraseña, self.correo,
                    self.wifi, self.redMovil
                ])
            print("Celular guardado en CSV correctamente.")
        except Exception as e:
            print(f"Error al guardar el celular en CSV: {e}")



    # Numero propio es el numero de la persona usando el celular
    def menu(self): #Este menú es del celular, las opciones que vería uno al interactuar con un celular, no el menú que nos permite seleccionar qué celular usar y esas cosas, eso es la clase Menu
        self.prendido = True #Esto es para asegurarse de que el valor se encuntre prendido, ya que puede estar apagado al instanciarse

        while self.prendido and self.bloqueado:
            print("\n--- Aplicaciones ---")
            print("1. Mensajes")
            print("2. Telefono")
            print("3. Configuracion")
            print("4. Mail")
            print("5. Contactos")
            print("6. Appstore")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                sms=SMS()
                sms.abrirApp()
                sms.menuSMS(self.numero,self.central)
                
            elif opcion == "2":
                tel = Telefono()
                tel.abrirApp()
                tel.menuLlamadas(self.central)

            elif opcion == "3":
                config = Configuracion()
                config.abrirApp()
                config.menuConfig()

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
            


    def validarId(id):
        if id not in Celular.ids:
            Celular.ids.add(id)
            return id
        else: raise ValueError('ya existe el id')

    # def registrar(self):
    #     self.registrado = True

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


#central1=Central()

