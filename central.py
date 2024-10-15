from aplicacion import SMS

class Central:
    def __init__(self):
        self.dispositivos_registrados = {}  # Diccionario de dispositivos registrados
                                            # La key es el numero, el celular(objeto) es el dato

    def registrarDispositivo(self,telefono):
        if telefono.numero not in self.dispositivos_registrados:
            self.dispositivos_registrados[telefono.numero] = telefono
            print(f"Teléfono {telefono.numero} registrado en la red.")
        else:
            print(f"El teléfono {telefono.numero} ya está registrado.")

    def eliminarDispositivo(self, telefono):
        if telefono.numero in self.dispositivos_registrados:
            del self.dispositivos_registrados[telefono.numero]
            print(f"Teléfono {telefono.numero} eliminado de la red.")
        else:
            print(f"El teléfono {telefono.numero} no está registrado.")

    def verificarDisponibilidad(self, telefono):
        if telefono.numero in self.dispositivos_registrados and telefono.encendido:
            print(f"El teléfono {telefono.numero} está disponible.")
            return True
        else:
            print(f"El teléfono {telefono.numero} no está disponible.")
            return False

    def gestionarLlamada(self, telefono_origen, telefono_destino):
        if self.verificarDisponibilidad(telefono_origen) and self.verificarDisponibilidad(telefono_destino):
            print(f"Estableciendo llamada entre {telefono_origen.numero} y {telefono_destino.numero}.")
            telefono_destino.recibirLlamada(telefono_origen.numero)
        else:
            print("No se puede establecer la llamada, uno o ambos dispositivos no están disponibles.")

    def gestionarSms(self, telefono_origen, telefono_destino, mensaje):
        if self.verificarDisponibilidad(telefono_origen) and self.verificarDisponibilidad(telefono_destino):
            print(f"Enviando mensaje desde {telefono_origen.numero} a {telefono_destino.numero}.")
            telefono_destino.recibirSms(telefono_origen.numero, mensaje)
            telefono_destino.sms
        else:
            print("No se puede enviar el mensaje, uno o ambos dispositivos no están disponibles.")
