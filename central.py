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
            self.disponibilidadDispositivos[numeroCelular] = True #un celular esta disponible cunado no esta en llamada
            print(f"Telefono numero registrado en la red.")
            try:
                with open('telefonosRegistrados.csv','a',newline='') as archivo:
                    writer = csv.writer(archivo)
                    writer.writerow([str(numeroCelular)])
            except: #FileNotFoundError('no se encontro el archivo de chats') as e:
                print('Error, archivo de chats no encontrado ')  
        else:
            raise KeyError(f"El telefono {numeroCelular} ya esta registrado.")
        
    def eliminarDispositivo(self, numeroCelular):
        if numeroCelular in self.dispositivos_registrados:
            self.dispositivos_registrados.remove(numeroCelular)
            print(f"Telefono {numeroCelular} eliminado de la red.")
        else:
            print(f"El telefono {numeroCelular} no esta registrado.")

    def verificarDisponibilidad(self, numeroCelular): #determina si esta o no en llamada
        if self.disponibilidadDispositivos.get(numeroCelular):
            return True
        else:
            return False

    def agregarContacto(self):
        pass
    
    def gestionarLlamada(self,numeroOrigen,numeroDestino,duracion):
        try:
            with open('llamadas.csv','a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(numeroOrigen),str(numeroDestino),duracion])
        except FileNotFoundError('No se encontro el archivo de historial de llamadas') as e:
            print(e)
    
    def leerLlamadas(self,numeroOrigen):
        llamadas = deque()
        try:
            with open('llamadas.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                for line in reader:
                    if line:
                        if line[0] == str(numeroOrigen):
                                llamadas.append((line[0],line[1],line[2]))
                        elif line[1] == str(numeroOrigen):
                                llamadas.append((line[0],line[1],line[2]))
            return llamadas
        except Exception('archivo no encontrado') as e:
            print(e)

    def gestionarSms(self,numeroOrigen,numeroDestino,mensaje): #A este metodo se le debe alimentar un objeto de la clase SMS, no celular
        if numeroDestino == 11: #los celulares se pueden registrar mensajeando al 011
            try:
                self.registrarDispositivo(numeroOrigen)
            except KeyError as e:
                print(e)
        elif self.verificarRegistro(numeroOrigen): 
            if self.verificarRegistro(numeroDestino):
                print(f"Enviando mensaje desde {numeroOrigen.numero} a {numeroDestino.numero}.")
                try:
                    with open('chats.csv','a',newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([str(numeroOrigen),str(numeroDestino),mensaje])
                except FileNotFoundError('no se encontro el archivo de chats') as e:
                    print('Error, archivo de chats no encontrado ')
            else:
                    print("El celular al que quiere contactar no esta registrado")
        else:
            raise ValueError('El celular no esta registrado')

    def eliminarSms(self,mensaje):
        try:
            rows = []
            with open('chats.csv','r',newline='') as file:
                reader = csv.reader(file)
                header = next(reader)
                rows.append(header)

                for row in reader:
                    if row[2] != mensaje:
                        rows.append(row)
                        
            with open("chats.csv","w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows) 

        except:
            print('Error, archivo de chats no encontrado ')
    
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
        

    def gestionarMail(self, direccion_origen, direccion_destino, titulo, mensaje, escencial, abierto): #A este metodo se le debe alimentar un objeto de la clase Mail, no celular
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
    



def verificarRegistro(self,numeroCelular): #pasar el get del numero de telefono si se tiene solo el numero
    if numeroCelular in self.dispositivos_registrados:
        return True
    else:
        return False