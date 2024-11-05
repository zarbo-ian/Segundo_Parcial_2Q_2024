import csv
from collections import deque
class Central:
    def __init__(self):
        self.dispositivos_registrados = set()  # Numeros de celular registrado
                                            

    def registrarDispositivo(self,numeroCelular): #hay que cambiar todo porque tiene que getear del diccionario las cosas
        if numeroCelular not in self.dispositivos_registrados:
            self.dispositivos_registrados.add(numeroCelular)
            print(f"Teléfono numero  registrado en la red.")
            
        else:
            raise KeyError(f"El teléfono {numeroCelular} ya está registrado.")
        
    def eliminarDispositivo(self, numeroCelular):
        if numeroCelular in self.dispositivos_registrados:
            self.dispositivos_registrados.remove(numeroCelular)
            print(f"Teléfono {numeroCelular} eliminado de la red.")
        else:
            print(f"El teléfono {numeroCelular} no está registrado.")

    def verificarDisponibilidad(self, celular):
        if celular.numero in self.dispositivos_registrados: #and celular.prendido:
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

    def gestionarSms(self,numeroOrigen,numeroDestino,mensaje): #A este método se le debe alimentar un objeto de la clase SMS, no celular
        if numeroDestino == 11: #los celulares se pueden registrar mensajeando al 011
            try:
                self.registrarDispositivo(numeroOrigen)
            except KeyError as e:
                print(e)
        else: #self.verificarRegistro(numeroOrigen): 
            #if self.verificarRegistro(numeroDestino):
            #print(f"Enviando mensaje desde {numeroOrigen.numero} a {numeroDestino.numero}.")
            try:
                with open('chats.csv','a',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([str(numeroOrigen),str(numeroDestino),mensaje])
            except: #FileNotFoundError('no se encontro el archivo de chats') as e:
                print('Error, archivo de chats no encontrado ')
            #else:
                    #print("El celular al que quiere contactar no esta registrado")
        #else:
            #raise ValueError('El celular no esta registrado')
    
    def leerSms(numeroOrigen):
        chats = dict()
        try:
            with open('chats.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                for line in reader:
                    if line:
                        if line[0] == str(numeroOrigen):
                            if int(line[1]) not in chats:
                                bandeja = deque()
                                bandeja.append((line[0],line[1],line[2]))                        
                                chats[line[1]] = bandeja
                            else:
                                chats.get([line[1]]).append((line[0],line[1],line[2]))
                        elif line[1] == str(numeroOrigen):
                            if int(line[0]) not in chats:
                                bandeja = deque()
                                bandeja.append((line[0],line[1],line[2]))
                                chats[line[0]] = bandeja
                            else:
                                chats.get([line[0]]).append((line[0],line[1],line[2]))
            return chats
        except: #Exception('archivo no encontrado') as e:
            print('error')
        

    def gestionarMail(self, direccion_origen, direccion_destino, titulo, mensaje, escencial, abierto): #A este método se le debe alimentar un objeto de la clase Mail, no celular
        #print(f"Mail enviado desde {direccion_origen.direccion} a {direccion_destino.direccion}.")
        try:
            with open("mails","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerow([direccion_origen,direccion_destino,titulo,mensaje,str(escencial)],str(abierto))
        except Exception as e:
            print(e)

# Verifica si amprint("Error")numeros estan registrados
    def verificarRegistroMensajes(self,celular_origen,numero_origen,numero_destino,mensaje):
        if numero_origen in self.dispositivos_registrados:
            print(f"El numero {numero_origen} esta registrado")
            return True
        else:
            print(f"El numero {numero_destino} no esta registrado")
            return False
        

# Verifica si los numeros estan registros
    def verificarRegistro(self,idCelular): #pasar el get del numero de telefono si se tiene solo el numero
        if idCelular in self.dispositivos_registrados:
            return True
        else:
            return False