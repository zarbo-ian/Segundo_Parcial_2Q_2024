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

    def cerrar(self): 
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
            if otroTelefono.telefono.ocupado == False:
                self.ocupado = True
                pass
            else:print('no esta disponible')
        else: print('Este telefono ya esta en llamada')
    
    def recibirLlamada(self,otroTelefono):
        self.ocupado = True
    
    def cortar(self,otroTelefono):
        pass


# DiccionarioChats guarda en clave otros celulares y en value una tupla compuesta por (Quien mando el mensaje, mensaje)
class SMS(Aplicacion): 
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool,ocupado):
        super().__init__(nombre, escencial, espacio, abierto)
        self.diccionarioChats={}
        self.nombre = 'SMS'
    
    def menuSMS(self,celular_origen,central,numero_origen): #pasarle los datos necesarios telefono remitente etc
        while self.prendido and self.desbloqueado:
            numero_destino = input("Ingresa el número de teléfono: ")
            mensaje = input("Escribe el mensaje: ")
            self.central.verificarRegistroMensajes(celular_origen,numero_origen,numero_destino,mensaje)
            


    def enviarMensaje(self,numero,mensaje):
        if numero not in self.diccionarioChats.keys():
            self.diccionarioChats[numero] = [(numero,mensaje)]
        else:
            self.diccionarioChats.get(numero).append((numero,mensaje))
        print(self.diccionarioChats)

    def recibirMensaje(self,numero_remitente,numero_destinatario,mensaje):
        if numero_remitente not in self.diccionarioChats:
            self.diccionarioChats[numero_remitente] = [(numero_remitente,mensaje)]
        else:
            self.diccionarioChats.get(numero_remitente).append((numero_remitente,mensaje))
        print(self.diccionarioChats)


class Mail(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, escencial, espacio, abierto)
        self.nombre = 'Mail'

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
            raise ValueError ('No se puede agendar ese numero porque ya esta agendado, pruebe actualizando el contacto')

# Actualiza el contacto y nombre en el diccionario
    def actualizarContacto(self,numero,nombre):
        if numero not in self.diccionario.keys():
            raise ValueError ("Ese numero no existe, intente agendarlo")
        else:
            self.diccionario[numero]=nombre

# Elimina el contacto de diccionario
    def eliminarContacto(self,numero):
        if numero not in self.diccionario.keys():
            raise ValueError('Este numero no esta agendado')
        else:
            self.diccionario.pop(numero)

class Configuracion(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, escencial, espacio, abierto)

    def activarRedMovil(self, cel):
        cel.redMovil = True #La red movil es un atributo del celular, por lo que cel es un objeto del tipo celular
    def desactivarRedMovil(self, cel):
        cel.redMovil = False        
        

class AppStore(Aplicacion):
    def __init__(self, nombre: str, escencial: bool, espacio: int, abierto: bool):
        super().__init__(nombre, escencial, espacio, abierto)
    def descargarAplicacion(self,celular,app):
        if app not in celular.aplicaciones:
            celular.aplicaciones.add(app)

