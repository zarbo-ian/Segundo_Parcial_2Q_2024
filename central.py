from aplicacion import SMS
from celular import *

class Central:
    def __init__(self):
        self.dispositivos_registrados = {}  # Diccionario de dispositivos registrados
                                            # La key es el numero, el celular(objeto) es el dato

    def registrarDispositivo(self,celular):
        if celular.numero not in self.dispositivos_registrados:
            self.dispositivos_registrados[celular.numero] = celular
            print(f"Teléfono {celular.numero} registrado en la red.")
            celular.registrar()
        else:
            print(f"El teléfono {celular.numero} ya está registrado.")

    def eliminarDispositivo(self, celular):
        if celular.numero in self.dispositivos_registrados:
            del self.dispositivos_registrados[celular.numero]
            print(f"Teléfono {celular.numero} eliminado de la red.")
        else:
            print(f"El teléfono {celular.numero} no está registrado.")

    def verificarDisponibilidad(self, celular):
        if celular.numero in self.dispositivos_registrados and celular.prendido:
            #print(f"El teléfono {celular.numero} está disponible.")
            return True
        else:
            print(f"El teléfono {celular.numero} no está disponible.")
            return False

    def gestionarLlamada(self, celular_origen, celular_destino): #A este método se le debe alimentar un objeto de la clase Telemono, no celular
        if self.verificarDisponibilidad(celular_origen) and self.verificarDisponibilidad(celular_destino) and celular_destino.disponible:
            print(f"Estableciendo llamada entre {celular_origen.numero} y {celular_destino.numero}.")
            celular_destino.ocupado = True
            celular_origen.ocupado = True
            celular_destino.recibirLlamada(celular_origen.numero)
        else:
            print("No se puede establecer la llamada, uno o ambos dispositivos no están disponibles.")

    def gestionarSms(self, celular_origen, celular_destino, mensaje): #A este método se le debe alimentar un objeto de la clase SMS, no celular
        if self.verificarDisponibilidad(celular_origen) and self.verificarDisponibilidad(celular_destino):
            print(f"Enviando mensaje desde {celular_origen.numero} a {celular_destino.numero}.")
            celular_destino.recibirMensaje(celular_origen.numero, mensaje)
        else:
            print("No se puede enviar el mensaje, uno o ambos dispositivos no están disponibles.")

    def gestionarMail(self, celular_origen, celular_destino, mensaje): #A este método se le debe alimentar un objeto de la clase Mail, no celular
        if self.verificarDisponibilidad(celular_origen) and self.verificarDisponibilidad(celular_destino):
            print(f"Enviando mail desde {celular_origen.mail_adress} a {celular_destino.mail_adress}.")
            celular_destino.recibirMail(celular_origen.mail_adress, mensaje)
        else:
            print("No se puede enviar el mensaje, uno o ambos dispositivos no están disponibles.")

# Verifica si ambos numeros estan registrados
    def verificarRegistroMensajes(self,celular_origen,numero_origen,numero_destino,mensaje):
        if not self.verificarRegistro(numero_origen):
            print(f"El numero {numero_origen} no esta registrado")
            return False
        elif not self.verificarRegistro(numero_destino):
            print(f"El numero {numero_destino} no esta registrado")
            return False
        else:
            celular_origen.sms.

# Verifica si los numeros estan registros
    def verificarRegistro(self,celular): #pasar el get del numero de telefono si se tiene solo el numero
        if celular.verificarRegistrado():
            return True
        else:
            return False