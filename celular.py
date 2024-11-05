from aplicacion import SMS, Mail, Configuracion, AppStore, Telefono, Contacto
from central import Central
from aplicacion import SMS
import numpy as np
import csv
#from tpEDP import Interfaz


class Celular:
    ids=set()
    def __init__(self,central, id:int, nombre:str, modelo:str, OS:str, RAM:int, almacenamiento:int, numero:int, prendido:bool, bloqueado:bool, contraseña: int, correo:str,wifi:bool, redMovil:bool, ocupado:bool=False, chatMensajes:list = None):
        self.id=id
        self.nombre=nombre
        self.modelo=modelo
        self.OS=OS
        self.RAM=RAM #En GB
        self.almacenamiento=almacenamiento #En GB, almacenamiento de fabrica
        self.almacenamientodisp= self.almacenamiento #En GB, almacenamiento disponible para aplicaciones no esenciales
        self.numero=numero
        self.prendido=False
        self.bloqueado=True
        self.contraseña=contraseña
        self.correo=correo # direccion de correo personal asociado al celular
        self.wifi=False
        self.redMovil=False
        #self.registrado = False #el celular no esta registrado en un principio
        self.chatMensajes={}
        self.central=central

        self.sms=SMS('SMS',True,1,False,self.id,self.numero,self.central)
        self.mail=Mail('Mail',True,1,False,self.correo)
        self.configuracion=Configuracion('Configuracion',True,1,False)
        self.appstore=AppStore('Appstore',True,1,False)
        self.telefono = Telefono('Telefono',True,1,False)
        self.contacto = Contacto('Contactos',True,1,False)
        self.aplicaciones={'SMS':self.sms, 'Mail':self.mail, 'Configuracion':self.configuracion, 'Appstore':self.appstore,'Telefono': self.telefono} # Todas las aplicaciones del celular
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

    #Si el celular no está prendido, pregunta si desea prenderlo        
        if not self.prendido:
            prender_celular=input("1. Prender\n2. Salir\n")
            if prender_celular=="1":
                self.prendido = True
                print("Has prendido el celular")
            else:
                print("No se ha prendido el celular")
                return

        if self.prendido:

            #La variable continuar hace que el flujo sea constante y cuando se decide salir del celular, este se bloquea
            continuar=True
            while continuar:
                print("\n1. Apagar celular")
                print("2. Bloquear celular")
                print("3. Acceder mediante contraseña")
                eleccion=input("Elija una opcion: ")
                if eleccion=="1":
                    self.prenderApagar()
                    print("Se ha apagado el celular")
                    continuar=False

                elif eleccion=="2":
                    self.bloqueado=True
                    print("Se ha bloqueado el celular")
                    continuar=False
                
                elif eleccion=="3":

                    # Intenta poner la contraseña hasta que decida salir
                    intento_contraseña=True
                    
                    # Permite entrar a las Apps cuando se ponga la contraseña correcta
                    permiso_aplicaciones=False

                    while intento_contraseña:
                        contraseña_puesta=input("Escriba su contraseña o toque ENTER para salir")
                        if contraseña_puesta=="":
                            intento_contraseña=False
                        elif contraseña_puesta!=self.contraseña:
                            print("Contraseña incorrecta, siga intentando")
                        elif contraseña_puesta==self.contraseña:
                            permiso_aplicaciones=True
                            intento_contraseña=False
                        
                    while permiso_aplicaciones:
                        print("\n--- Aplicaciones ---")
                        print("1. Mensajes")
                        print("2. Telefono")
                        print("3. Configuracion")
                        print("4. Mail")
                        print("5. Contactos")
                        print("6. Appstore")
                        print("7. Salir")

                        opcion = input("Elige una opción: ")

                        if opcion == "1":
                            if self.redMovil==False and self.wifi==False:
                                print("Antes de acceder a esta App, prende su Red Movil o WIFI")
                            else:
                                self.sms.menuSMS(self,central1)
                            
                        elif opcion == "2":
                            if self.redMovil==False and self.wifi==False:
                                print("Antes de acceder a esta App, prende su Red Movil o WIFI")
                            else:
                                self.telefono.menuLlamadas(self)

                        elif opcion == "3":
                            self.configuracion.menuConfig(self)

                        elif opcion == "4":
                            if self.redMovil==False and self.wifi==False:
                                print("Antes de acceder a esta App, prende su Red Movil o WIFI")
                            else:
                                self.mail.menuMail(self)
                        
                        elif opcion == "5":
                            self.contacto.menuContacto(self)

                        elif opcion == "6":
                            if self.redMovil==False and self.wifi==False:
                                print("Antes de acceder a esta App, prende su Red Movil o WIFI")
                            else:
                                self.appstore.menuApp
                        
                        elif opcion=="7":
                            permiso_aplicaciones=False
                        
                        else:
                            print("Esa opcion no es valida")
                else:
                    print("Opcion no valida")

            print("Has salido")

    @classmethod
    def cargar_ids(self):
        try:
            with open('celulares.csv','r',newline='') as archivo:
                lector=csv.reader(archivo)
                next(lector)
                for i in lector:
                    self.ids.add(i[0])
        except:
            pass
        
    @classmethod
    def validarId(self,id):
        if id not in Celular.ids:
            Celular.ids.add(id)
        else:
            raise ValueError('No puede usar un id existente')


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


central1=Central()

