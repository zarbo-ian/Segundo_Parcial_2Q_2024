import aplicacion

class Celular:
    def __init__(self, id:int, nombre:str, modelo:str, OS:str, RAM:int, almacenamiento:int, numero:int, prendido:bool, bloqueado:bool, contraseña: int, ocupado:bool, mail:str,wifi:bool, redMovil:bool):
        self.id=id
        self.nombre=nombre
        self.modelo=modelo
        self.OS=OS
        self.RAM=RAM #En GB
        self.almacenamiento=almacenamiento #En GB
        self.numero=numero
        self.prendido=prendido
        self.bloqueado=bloqueado
        self.contraseña=contraseña
        self.mail=mail 
        self.ocupado=ocupado
        self.wifi=wifi
        self.redMovil=redMovil #
        self.aplicaciones=set()
        self.registrado = False #acordarse de cambiar a true al registrar

    def prenderApagar(self): #un mismoo boton prende y apaga el cle
        if self.prendido: #Si está prendido se apaga
            self.prendido = False
        else: #Si está apagado se prende
            self.prendido = True
            self.bloquear() #despues de prender el celular hay que reingresar la contraseña
            self.ocupado = False

            #cuando se prenda debe activarse la red movil
            if self.registrado == True:
                self.redMovil = True

            #preguntar SI DAR UN CELULAR DE BAJA ELIMINA LA INSTANCIA

            
    
    def desbloquear(self, pass_given):
        if self.bloqueado:
            if pass_given==self.contraseña:
                self.bloqueado=False
            else:
                raise Exception("Contraseña incorrecta, vuelve a intentarlo")
        else:
            raise Exception('El telefono ya estaba desbloqueado')
            
    def bloquear(self):
        self.bloqueado=True
    
    def verificarPrendido(self): #es necesario saber si esta prendido para recibir llamadas 
        return self.prendido
    
    def verificarOcupado(self):
        if self.prendido:
            return self.ocupado
    
    def verificarWifi(self):
        if self.prendido:
            return self.wifi

    def verificarRedmovil(self):
        if self.prendido:
            return self.redMovil