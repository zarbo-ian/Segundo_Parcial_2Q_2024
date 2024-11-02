from celular import * #esto deberia se al reves, el celular deberia importar la central

class Central:
    def __init__(self):
        self.dispositivos_registrados = set()  # Diccionario de dispositivos registrados deberia ser un set
                                            # La key es el numero, el celular(objeto) es el dato

    def registrarDispositivo(self,idCelular,numeroCelular): #hay que cambiar todo porque tiene que getear del diccionario las cosas
        if idCelular.numero not in self.dispositivos_registrados:
            self.dispositivos_registrados[numeroCelular] = idCelular
            print(f"Teléfono numero  registrado en la red.")
            idCelular.registrar()
        else:
            raise KeyError(f"El teléfono {idCelular.numero} ya está registrado.")
        
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

    def gestionarLlamada(self, idcelular_origen,celular_origen,idcelular_destino, celular_destino): #necesita el id del celular y el numero de telefono
        if self.verificarDisponibilidad(celular_origen):
            if self.verificarDisponibilidad(celular_destino) and celular_destino.disponible:
                print(f"Estableciendo llamada entre {celular_origen.numero} y {celular_destino.numero}.")
                celular_destino.recibirLlamada(celular_origen.numero)
            else:
                print('El numero al que se esta intentando llamar no esta disponible')
        else:
            print('El celular intentando llamar esta ocupado')

    def gestionarSms(self, idcelular_origen,celular_origen, celular_destino, mensaje): #A este método se le debe alimentar un objeto de la clase SMS, no celular
        if celular_destino == 11: #los celulares se pueden registrar mensajeando al 011
            try:
                self.registrarDispositivo(idcelular_origen,celular_origen)
            except KeyError as e:
                print(e)
            else:
                pass
            finally:
                pass
        elif self.verificarDisponibilidad(celular_origen): 
            if self.verificarDisponibilidad(celular_destino):
                print(f"Enviando mensaje desde {celular_origen.numero} a {celular_destino.numero}.")
                #aca deberia haber algo que cargue a la nube el mensaje, asi lo puede leer el celular destino al prender sms
            else:
                    print("El celular al que quiere contactar no esta registrado")
        else:
            pass
            raise ValueError('el celular no esta registrado')
        

    def gestionarMail(self, celular_origen, celular_destino, mensaje): #A este método se le debe alimentar un objeto de la clase Mail, no celular
        if self.verificarDisponibilidad(celular_origen) and self.verificarDisponibilidad(celular_destino):
            print(f"Enviando mail desde {celular_origen.mail_adress} a {celular_destino.mail_adress}.")
            celular_destino.recibirMail(celular_origen.mail_adress, mensaje)
        else:
            print("No se puede enviar el mensaje, uno o ambos dispositivos no están disponibles.")

# Verifica si ambos numeros estan registrados
    def verificarRegistroMensajes(self,celular_origen,numero_origen,numero_destino,mensaje):
        if numero_origen in self.dispositivos_registrados:
            print(f"El numero {numero_origen} esta registrado")
            return True
        else:
            print(f"El numero {numero_destino} no esta registrado")
            return False
        

# Verifica si los numeros estan registros
    def verificarRegistro(self,celular): #pasar el get del numero de telefono si se tiene solo el numero
        if celular in self.dispositivos_registrados:
            return True
        else:
            return False