from celular import Celular
import csv
from central import Central

class Main:
    def __init__(self):
        self.central=Central()
        # Diccionario para almacenar instancias de celulares cargados desde el CSV
        self.celulares = {}
        # Cargar los datos existentes del CSV al iniciar el programa
        self.cargar_celulares_csv()
        Celular.cargar_ids()
    
    def mostrar_menu(self):
        "Muestra el menu principal del programa y gestiona las opciones."
        while True:
            print("\n--- Menu Principal ---")
            print("1. Aniadir un nuevo celular")
            print("2. Acceder a un celular existente")
            print("3. Salir")
            
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                self.agregar_celular()
            elif opcion == "2":
                try:
                    acceder_id = input("Ingrese el ID del celular que desea acceder: ")
                    self.acceder_celular(acceder_id)
                except:
                    print("Ese celular no existe")
            elif opcion == "3":

                # Rescribe el csv en base a los celulares guardados en diccionario (los cuales estan actualizados)
                with open('celulares.csv','w',newline='') as archivo:
                    escritor=csv.writer(archivo)
                    escritor.writerow(['ID', 'Nombre', 'Modelo', 'OS', 'RAM', 'Almacenamiento','Numero', 'Prendido', 'Bloqueado', 'Contrasena','Correo', 'WiFi', 'Red Movil'])
                    for celular in self.celulares.values():
                        escritor.writerow([celular.id,celular.central, celular.nombre,celular.modelo,celular.OS,celular.RAM,celular.almacenamiento,celular.numero,celular.prendido,celular.bloqueado,celular.contrasenia,celular.correo,celular.wifi,celular.redMovil])
                        print(celular.wifi)

                print("Saliendo del programa.")
                return
            else:
                print("Opcion invalida. Intente de nuevo.")

    def agregar_celular(self):
        "Solicita datos al usuario para aniadir un nuevo celular y lo guarda en el CSV."
        id = input("ID: ")
        Celular.validarId(id)
        nombre = input("Ingrese el nombre del celular: ")
        modelo = input("Ingrese el modelo del celular: ")
        OS = input("Ingrese el sistema operativo (OS): ")
        RAM = int(input("Ingrese la RAM en GB: "))
        almacenamiento = int(input("Ingrese el almacenamiento en GB: "))
        numero = input("Ingrese el numero de telefono: ")
        prendido = False
        bloqueado = True
        contrasenia = input("Ingrese la contrasenia del celular: ")
        correo = input("Ingrese el correo electronico asociado: ")
        wifi = False
        redMovil = True

        # Crear y guardar la instancia del celular
        nuevo_celular = Celular(
            id, self.central, nombre, modelo, OS, RAM, almacenamiento, numero, prendido, bloqueado, 
            contrasenia, correo, wifi, redMovil
        )
        nuevo_celular.guardar_en_csv()
        self.celulares[id] = nuevo_celular
        print("Celular aniadido y guardado en CSV.")
    
    def guardar_en_csv(self):
        with open("celulares.csv",mode="a",newline='') as  archivo:
            escritor=csv.writer(archivo)
            if archivo.tell() == 0:  # Verifica si el archivo esta vacio
                escritor.writerow(['ID', 'Nombre', 'Modelo', 'OS', 'RAM', 'Almacenamiento','Numero', 'Prendido', 'Bloqueado', 'Contrasena','Correo', 'WiFi', 'Red Movil'])
            escritor.writerow([self.id, self.nombre, self.modelo, self.OS, self.RAM, self.almacenamiento, self.numero, self.prendido, self.bloqueado, self.contrasenia, self.correo, self.wifi, self.redMovil])

    def cargar_celulares_csv(self):
        try:
            with open("celulares.csv",mode="r",newline='') as archivo:
                lector=csv.reader(archivo)
                next(lector)
                for i in lector:
                    celular = Celular(i[0], self.central, i[1], i[2], i[3], int(i[4]), int(i[5]), i[6], i[7] == "True", i[8] == "True", i[9], i[10], i[11] == "True", i[12] == "True")
                    self.celulares[i[0]]=celular
        except:
            pass
    
    def acceder_celular(self,id):
        celular=self.celulares.get(id)
        celular.menu()

# Inicializar y ejecutar el programa
if __name__ == "__main__":
    main = Main()
    main.mostrar_menu()
