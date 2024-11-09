import csv
from collections import deque
class Central:
    def __init__(self):
        self.dispositivos_registrados = set()  # Numeros de celular registrado
        self.disponibilidadDispositivos = dict() #Diccionario con clave celular,valor booleano True: Disponible False: Ocupado(en llamada)
        self.bajarRegistrados()
    
    def bajarRegistrados(self):
        try:
            with open('telefonosRegistrados.csv','r',newline='') as archivo:
                    lector=csv.reader(archivo)
                    for i in lector:
                        self.dispositivos_registrados.add(i)
        except FileNotFoundError:
            with open('telefonosRegistrados.csv','w',newline='') as archivo:
                pass
  
    def registrarDispositivo(self,numeroCelular): #hay que cambiar todo porque tiene que getear del diccionario las cosas
        if numeroCelular not in self.dispositivos_registrados:
            self.dispositivos_registrados.add(numeroCelular)
            self.disponibilidadDispositivos[numeroCelular] = True
            print(f"Teléfono numero registrado en la red.")
            try:
                with open('telefonosRegistrados.csv','a',newline='') as archivo:
                    writer = csv.writer(archivo)
                    writer.writerow([str(numeroCelular)])
            except: #FileNotFoundError('no se encontro el archivo de chats') as e:
                print('Error, archivo de chats no encontrado ')  
        else:
            raise KeyError(f"El teléfono {numeroCelular} ya está registrado.")
        
    def eliminarDispositivo(self, numeroCelular):
        if numeroCelular in self.dispositivos_registrados:
            self.dispositivos_registrados.remove(numeroCelular)
            print(f"Teléfono {numeroCelular} eliminado de la red.")
        else:
            print(f"El teléfono {numeroCelular} no está registrado.")

    def verificarDisponibilidad(self, numeroCelular): #determina si esta o no en llamada
        if self.disponibilidadDispositivos.get(numeroCelular):
            return True
        else:
            return False

    def agregarContacto(self):
        pass

    

    # def gestionarLlamada(self,celular_origen,celular_destino): #necesita el id del celular y el numero de telefono
    #     if self.verificarDisponibilidad(celular_origen):
    #         if self.verificarDisponibilidad(celular_destino) and celular_destino.disponible:
    #             print(f"Estableciendo llamada entre {celular_origen.numero} y {celular_destino.numero}.")
    #             celular_destino.recibirLlamada(celular_origen.numero)
    #         else:
    #             print('El numero al que se esta intentando llamar no esta disponible')
    #     else:
    #         print('El celular intentando llamar esta ocupado')

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

    def visualizar_mails_leidos(self):
        recibidos_no_leidos = []
        recibidos_leidos = []
        try:
            with open("mails.csv","r",newline="") as file:
                reader = csv.reader(file)
                for line in reader:
                    if line[1] == self.direccion:
                        if eval(line[5]) == False:
                            recibidos_no_leidos.insert(0,(line[0],line[2],line[3],line[4],line[5]))
                        else:
                            recibidos_leidos.insert(0,(line[0],line[2],line[3],line[4],line[5]))
            return recibidos_no_leidos, recibidos_leidos
        except Exception as e:
            print(e)
                
    def visualizar_mails_tiempo(self):
        recibidos = []
        try:
            with open("mails.csv","r",newline="") as file:
                reader = csv.reader(file)
                for line in reader:
                    if line[1] == self.direccion:
                        recibidos.insert(0,(line[0],line[2],line[3],line[4],line[5]))
            return recibidos
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
    def verificarRegistro(self,numeroCelular): #pasar el get del numero de telefono si se tiene solo el numero
        if numeroCelular in self.dispositivos_registrados:
            return True
        else:
            return False