"""
Implemente la clase Pila, como una secuencia de nodos anidados. En esta implementación el constructor de
la clase lista almacena la dirección al nodo cima.Los métodos de la clase Pila a realizar son: 
    Apilar, desapilar, esVacia, visualizar Pila.
En esta Pila usted tiene almacenada la información de los libros de una biblioteca que están llegando para
su organización y antes de ubicarlos en su librero se verifica su estado e información este completa.
De cada libro se debe tener: nombre/s autor, fecha de publicación, editorial y el número ISSN 
(código de 8 dígitos que sirven para identificar las publicaciones)
"""

class Nodo():
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
    def __str__(self) -> str:
        return str(self.dato)

class Lista():
    def __init__(self):
        self.head = None
        self.len = 0 # al crear la lista, no tiene nada

    def agregarInicio(self, nodo: Nodo):
        # si la lista está vacía, le agregamos un 1er nodo
        if self.len == 0:
            self.head = nodo
        # si no está vacía, le damos una nueva cabecera, pero sin desligarnos de los otros nodos que le siguen
        else:
            nodo.prox = self.head # con esto el próximo nodo al que apunta el ingresado es la actual cabecera, que aquí dejará de ser cabecera
            self.head = nodo # ahora si, el nodo ingresado es la nueva cabecera
        self.len += 1

    def __str__(self):
        nodo = self.head # nodo auxiliar, el 1ero de la lista
        cadena = ""
        if (self.len == 0):
            return "La lista está vacía"
        else:
            while(nodo != None): #con esto nos fijamos que el nodo exista
                cadena += str(nodo.dato) + "\t"
                nodo = nodo.prox # ahora apuntamos al siguiente nodo de la lista
            return cadena
        
    def append(self, nodo: Nodo):
        if(self.len == 0):
            self.head = Nodo # Si la lista está vacía, el nodo ingresado será la nueva cabecera
        else:
            nodoMov = Nodo() # este nodo auxiliar lo usaré para moverme
            nodoMov = self.head # arrancaremos a iterar desde la cabecera
            while(nodoMov.prox != None):
                nodoMov = nodoMov.prox # paso al siguiente nodo ya que sabemos que existe
            # ya llegamos al último nodo, ahora este va a apuntar al nodo ingresado
            nodoMov.prox = nodo
        self.len += 1 

    def pop(self, pos = None): #si la posición es None, eliminamos el nodo de la última posición
        nodo = Nodo()
        nodo = self.head
        if(pos == None):
            final = self.len - 2 # tengo que moverme al anteultimo nodo para decirle que ahora apunte a None
            for i in range(final):
                nodo = nodo.prox
            nodo.prox = None
        else: #tengo que llegar a esa posición anterior a la asignada y hacer un puente el nodo siguiente al que borramos
            for i in range(pos-1):
                nodo = nodo.prox
            #ahora ya estamos en la posición anterior al nodo que vamos a eliminar
            nodo.prox = nodo.prox.prox #el nuevo siguiente será el siguiente del siguiente (o sea el siguiente al eliminado)
        self.len -= 1

class Pila():
    def __init__(self, autor, publicacion, editorial, ISSN):
        self.autor = autor
        self.publicacion = publicacion
        self.editorial = editorial
        self.ISSN = ISSN
    def apilar(self):
        print("esto es para apilar")
    def desapilar(self):
        print("Para desapilar")
    def esVacia(self):
        print("hol")

listaLibros = Lista()