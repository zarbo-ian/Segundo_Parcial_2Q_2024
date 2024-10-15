# Funcionalidades de un telefono celular (ID,nombre,modelo,OS,version,RAM,almacenamiento,numero)

# Metodos del celular:
# Prender y apagarse (Mismo metodo que varia dependiendo del estado del telefono). Cuando se apaga el celular, se cierran todas las apps, deberiamos guaradar las apps en funcionamiento
# Bloquear y desbloquear (Mimso metodo que varia dependiendo del estado del telefono)
# Abrir una app (Contactos,SMS,mail,telefono,appStore,configuracion,etc)
# Descargar apps no basicas

# Metodos dentro de las apps:
# Telefono: Realizar llamadas, recibir llamadas, terminar una llamada, ver historial
# Contactos: Agendar y actualizar contactos (diccionario key: nro, value: nombre contacto)
# SMS: Enviar y recibir mensajes a un nro, ver bandeja de entradas, eliminar mensajes (pilas, ultimo mensaje me parece lo mejor)
# Mail: Ver mails no leidos (Lista enlazada que se borran a medida que se leen) y por fecha (un sorted)
# AppStore: Descargar una app
# Configuracion: Cambiar nombre del telefono y codigo de desbloqueo, activar red movil (cuando el celular se encienda), desactivar red movil,  activar y desactivar datos

# La gestion de llamadas y mensajes debe ser administrada por una central (En el tp, solo existe una)
# Como funcionan las llamadas y mensajes: Emisor envia a la central una solicitud de conexion con informacion (App origen, nro  destino, mensaje, etc), la central revisa si ambos estan registrados y disponibles, cuando se establece la conexion, los dispositivos pasan a administrar la llamada o mensaje 

# Metodos de la central: Verificar estado dispositivos, verificar que esten registrados, verificar estado dispositivos que quieran acceder a red, establecer y mediar la comunicacion, llevar un registro de las comunicaciones ()
# Como guarda le central a los telefonos y sus estados? Diccionarios?



class Aplicacion:
    def __init__(self, nombre:str):
        self.nombre=nombre

