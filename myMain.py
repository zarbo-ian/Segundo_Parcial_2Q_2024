from celular import Celular
import csv

class Main:
    def __init__(self):
        # Diccionario para almacenar instancias de celulares cargados desde el CSV
        self.celulares = {}
        # Cargar los datos existentes del CSV al iniciar el programa
        self.cargar_celulares_csv()
        # Mostrar menú inicial al usuario

    def mostrar_menu(self):
        continuar=True
        while continuar==True:
            print("\n--- Menú Principal ---")
            print("1. Añadir un nuevo celular")
            print("2. Acceder a un celular existente")
            print("3. Salir")
            
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_celular()
            elif opcion == "2":
                acceder_id=input("Ingrese el id cuyo celular quiere acceder: ")
                self.mostrar_celulares(acceder_id)
            elif opcion == "3":
                print("Saliendo del programa.")
                continuar=False
            else:
                print("Opción inválida. Intente de nuevo.")

    def agregar_celular(self):
        # Solicitar datos del celular al usuario
        id = input("ID: ")
        Celular.validarId(id)
        nombre = input("Ingrese el nombre del celular: ")
        modelo = input("Ingrese el modelo del celular: ")
        OS = input("Ingrese el sistema operativo (OS): ")
        RAM = int(input("Ingrese la RAM en GB: "))
        almacenamiento = int(input("Ingrese el almacenamiento de fábrica en GB: "))
        numero = input("Ingrese el número de teléfono: ")
        prendido = False
        bloqueado = True
        contraseña = input("Ingrese la contraseña del celular: ")
        correo = input("Ingrese el correo electrónico asociado: ")
        wifi = False
        redMovil = True

        # Crear y guardar la instancia del celular
        nuevo_celular = Celular(id, nombre, modelo, OS, RAM, almacenamiento, numero, prendido, bloqueado, contraseña, correo, wifi, redMovil)
        nuevo_celular.guardar_en_csv()
        self.celulares[id] = nuevo_celular
        print("Celular añadido y guardado en CSV.")
    
    def mostrar_celulares_csv(self,acceder_id):
        celulares = {}
        with open("celulares.csv", mode='r') as file:
            lector=csv.reader(file)
            file.readline()
            for fila in file:
                celulares[fila[0]]=Celular(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],[9],fila[10],fila[11],fila[12])
            if acceder_id in celulares:
                celulares[acceder_id].menu()
        print(celulares)

    def cargar_celulares_csv(self):
        # Leer los datos del CSV y crear instancias de Celular
        try:
            with open("celulares.csv", mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    celular = Celular(
                        id=row["ID"], nombre=row["Nombre"], modelo=row["Modelo"], OS=row["OS"],
                        RAM=int(row["RAM"]), almacenamiento=int(row["Almacenamiento"]),
                        numero=row["Numero"], prendido=row["Prendido"] == "True",
                        bloqueado=row["Bloqueado"] == "True", contraseña=row["Contraseña"],
                        correo=row["Correo"], wifi=row["WiFi"] == "True", redMovil=row["RedMovil"] == "True"
                    )
                    self.celulares[row["ID"]] = celular
        except FileNotFoundError:
            print("Archivo CSV no encontrado. Se creará uno nuevo al agregar celulares.")
main=Main()
main.mostrar_menu()