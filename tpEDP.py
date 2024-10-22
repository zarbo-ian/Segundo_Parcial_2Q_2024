#HACER MENU PARA TOD0

# Funcionalidades de un telefono celular (ID,nombre,modelo,OS,version,RAM,almacenamiento,numero)

# Metodos del celular:
# Prender y apagarse (Mismo metodo que varia dependiendo del estado del telefono). Cuando se apaga el celular, se cierran todas las apps, deberiamos guaradar las apps en funcionamiento
# Bloquear y desbloquear (Mimso metodo que varia dependiendo del estado del telefono)
# Abrir una app (Contactos,SMS,mail,telefono,appStore,configuracion,etc)
# Descargar apps no basicas

# Metodos dentro de las apps:
# Telefono: Realizar llamadas, recibir llamadas, terminar una llamada, ver historial
# Contactos: Agendar y actualizar contactos (diccionario key: nro, value: nombre contacto)
# SMS: Enviar y recibir mensajes a un nro, ver bandeja de entradas (lista de tuplas), eliminar mensajes (pilas, ultimo mensaje me parece lo mejor)
# Mail: Ver mails no leidos (Lista enlazada que se borran a medida que se leen) y por fecha (un sorted)
# AppStore: Descargar una app
# Configuracion: Cambiar nombre del telefono y codigo de desbloqueo, activar red movil (cuando el celular se encienda), desactivar red movil,  activar y desactivar datos

# La gestion de llamadas y mensajes debe ser administrada por una central (En el tp, solo existe una)
# Como funcionan las llamadas y mensajes: Emisor envia a la central una solicitud de conexion con informacion (App origen, nro  destino, mensaje, etc), la central revisa si ambos estan registrados y disponibles, cuando se establece la conexion, los dispositivos pasan a administrar la llamada o mensaje 

# Metodos de la central: Verificar estado dispositivos, verificar que esten registrados, verificar estado dispositivos que quieran acceder a red, establecer y mediar la comunicacion, llevar un registro de las comunicaciones ()
# Como guarda le central a los telefonos y sus estados? Diccionarios?


def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Enviar mensaje")
        print("2. Recibir mensaje")
        print("3. Llamar por teléfono")
        print("4. Ver historial de llamadas")
        print("5. Ver chats")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            numero = input("Ingresa el número de teléfono: ")
            mensaje = input("Escribe el mensaje: ")


        elif opcion == "2":
            celular = input("Ingresa tu número de celular: ")
            remitente = input("Ingresa el nombre del remitente: ")
            mensaje = input("Escribe el mensaje recibido: ")


        elif opcion == "3":
            numero = input("Ingresa el número al que deseas llamar: ")


        elif opcion == "4":
            print("\n--- Historial de Llamadas ---")


        elif opcion == "5":
            print("\n--- Chats ---")
            

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú
menu()