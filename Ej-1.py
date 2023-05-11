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

    def __init__(self,dato=None,prox=None):

        self.dato=dato

        self.prox=prox

    def __str__(self) -> str:

        return str(self.dato) # Especificas como queres que se printee

   

class Pila():

    def __init__(self):

        self.head=None

        self.len=0

       

    def __str__(self):

        nodo = Nodo()

        nodo=self.head

        lista = []

        while nodo is not None:

            lista.append(str(nodo.dato.__dict__))

            nodo = nodo.prox

        return "\n".join(lista)

   

    def append(self,nodo:Nodo):

        if(self.len==0):

            self.head=nodo

        else:

            nodo.prox=self.head

            self.head=nodo

        self.len+=1

   

    def pop(self):

        nodo=Nodo()

        nodo=self.head

        self.head=nodo.prox

        self.len-=1

       

 

class Cola():

    def __init__(self):

        self.head=None

        self.len=0

       

    def __str__(self):

        nodo = Nodo()

        nodo=self.head

        lista = []

        while nodo is not None:

            lista.append(str(nodo.dato.__dict__))

            nodo = nodo.prox

        return "\n".join(lista)

   

    def append(self,nodo:Nodo):

        if(self.len==0):

            self.head=nodo

        else:

            nodo.prox=self.head

            self.head=nodo

        self.len+=1

   

    def pop(self):

        nodo=Nodo()

        nodo=self.head

        self.head=nodo.prox

        self.len-=1

       

class Libro:

    def __init__(self,nombre_autor,fecha,editorial,numero_ISSN):

        self.nombre=nombre_autor

        self.fecha=fecha

        self.editorial=editorial

        self.numero_ISSN=numero_ISSN