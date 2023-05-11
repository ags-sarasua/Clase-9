"""
Implemente un programa que vaya apilando las cartas una debajo de la otra, pero solo permite apilarlas si
son de un número inmediatamente inferior y de distinto palo. Si se intenta apilar una carta incorrecta, se
debe dar una excepción. Adicionalmente, se debe contar con el método str que imprimirá las cartas
que se hayan apilado hasta el momento.
"""

from collections import deque

pila = deque()
