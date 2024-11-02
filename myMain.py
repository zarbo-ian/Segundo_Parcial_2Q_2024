from celular import Celular
import csv

class Main:
    def __init__(self):
        # Diccionario para almacenar instancias de celulares cargados desde el CSV
        self.celulares = {}
        # Cargar los datos existentes del CSV al iniciar el programa
        self.cargar_celulares_csv()
    
    def mostrar_menu(self):
        """Muestra el menú principal del programa y gestiona las opciones."""
        while True:
            print("\n--- Menú Principal ---")
            print("1. Añadir un nuevo celular")
            print("2. Acceder a un celular existente")
            print("3. Salir")
            
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_celular()
            elif opcion == "2":
                acceder_id = input("Ingrese el ID del celular que desea acceder: ")
            elif opcion == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    def agregar_celular(self):
        """Solicita datos al usuario para añadir un nuevo celular y lo guarda en el CSV."""
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
            id, nombre, modelo, OS, RAM, almacenamiento, numero, prendido, bloqueado, 
            contraseña, correo, wifi, redMovil
        )
        nuevo_celular.guardar_en_csv()
        self.celulares[id] = nuevo_celular
        print("Celular añadido y guardado en CSV.")
    
    def guardar_en_csv(self):
        with open("celulares.csv",mode="w",newline='') as  archivo:
            escritor=csv.writer(archivo)
            if archivo.tell() == 0:  # Verifica si el archivo está vacío
                escritor.writerow(['ID', 'Nombre', 'Modelo', 'OS', 'RAM', 'Almacenamiento','Número', 'Prendido', 'Bloqueado', 'Contraseña','Correo', 'WiFi', 'Red Móvil'])


# Inicializar y ejecutar el programa
if __name__ == "__main__":
    main = Main()
    main.mostrar_menu()
