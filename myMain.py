from celular import Celular
import csv
from random import randint
from central import Central

class Main:
    def __init__(self):
        # Diccionario para almacenar instancias de celulares cargados desde el CSV
        self.celulares = {}
        # Cargar los datos existentes del CSV al iniciar el programa
        self.cargar_celulares_csv()
        Celular.cargar_ids()
    
    def mostrar_menu(self):
        "Muestra el menú principal del programa y gestiona las opciones."
        while True:
            print("\n--- Menú Principal ---")
            print("1. Añadir un nuevo celular")
            print("2. Acceder a un celular existente")
            print("3. Salir")
            
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_celular()
            elif opcion == "2":
                try:
                    acceder_id = input("Ingrese el ID del celular que desea acceder: ")
                    self.acceder_celular(acceder_id)
                except:
                    print("Ese celular no exist")
            elif opcion == "3":

                # Rescribe el csv en base a los celulares guardados en diccionario (los cuales estan actualizados)
                with open('celulares.csv','w',newline='') as archivo:
                    escritor=csv.writer(archivo)
                    escritor.writerow(['ID', 'Nombre', 'Modelo', 'OS', 'RAM', 'Almacenamiento','Numero', 'Prendido', 'Bloqueado', 'Contrasena','Correo', 'WiFi', 'Red Movil'])
                    for celular in self.celulares.values():
                        escritor.writerow([celular.id,celular.nombre,celular.modelo,celular.OS,celular.RAM,celular.almacenamiento,celular.numero,celular.prendido,celular.bloqueado,celular.contraseña,celular.correo,celular.wifi,celular.redMovil])
                        print(celular.id)

                print("Saliendo del programa.")
                return
            else:
                print("Opción inválida. Intente de nuevo.")

    def agregar_celular(self):
        "Solicita datos al usuario para añadir un nuevo celular y lo guarda en el CSV."
        id = input("ID: ")
        Celular.validarId(id)
        nombre = input("Ingrese el nombre del celular: ")
        modelo = input("Ingrese el modelo del celular: ")
        OS = input("Ingrese el sistema operativo (OS): ")
        RAM = int(input("Ingrese la RAM en GB: "))
        almacenamiento = int(input("Ingrese el almacenamiento en GB: "))
        numero = input("Ingrese el número de teléfono: ")
        prendido = False
        bloqueado = True
        contraseña = input("Ingrese la contraseña del celular: ")
        correo = input("Ingrese el correo electrónico asociado: ")
        wifi = False
        redMovil = True

        # Crear y guardar la instancia del celular
        nuevo_celular = Celular(
            id,Central(), nombre, modelo, OS, RAM, almacenamiento, numero, prendido, bloqueado, 
            contraseña, correo, wifi, redMovil
        )
        nuevo_celular.guardar_en_csv()
        self.celulares[id] = nuevo_celular
        print("Celular añadido y guardado en CSV.")
    
    def guardar_en_csv(self):
        with open("celulares.csv",mode="a",newline='') as  archivo:
            escritor=csv.writer(archivo)
            if archivo.tell() == 0:  # Verifica si el archivo está vacío
                escritor.writerow(['ID', 'Nombre', 'Modelo', 'OS', 'RAM', 'Almacenamiento','Numero', 'Prendido', 'Bloqueado', 'Contrasena','Correo', 'WiFi', 'Red Movil'])
            escritor.writerow([self.id, self.nombre, self.modelo, self.OS, self.RAM, self.almacenamiento, self.numero, self.prendido, self.bloqueado, self.contraseña, self.correo, self.wifi, self.redMovil])

    def cargar_celulares_csv(self):
        dictCelulares={}
        try:
            with open("celulares.csv",mode="r",newline='') as archivo:
                lector=csv.reader(archivo)
                next(lector)
                for i in lector:
                    celular = Celular(i[0], i[2], i[3], int(i[4]), int(i[5]), i[6], i[7] == "True", i[8] == "True", i[9], i[10], i[11] == "True", i[12] == "True",i[13])
                    self.celulares[i[0]]=celular
        except:
            pass
            print(dictCelulares)
            print(self.celulares)
    
    def acceder_celular(self,id):
        celular=self.celulares.get(id)
        celular.menu()

# Inicializar y ejecutar el programa
if __name__ == "__main__":
    main = Main()
    main.mostrar_menu()
