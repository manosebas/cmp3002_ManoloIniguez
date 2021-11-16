#!/usr/bin/env python
# coding: utf-8

# ## Verdadero o falso con argumentos

# ### 1.  Una función recursiva resuelve un problema resolviendo una parte mas pequeña del mismo problema 

# In[1]:


#Verdadero, una función recursiva es una técnica que resuelve problemas usando una función 
#que se llama a si misma reduciendo el problema en subproblemas


# ### 2.  Los modelos computacionales nos ayudan a analizar la complejidad de los algoritmos, ya que nos proveen de las especificaciones de la computadora en la cual estos se ejecutarían idealmente

# In[ ]:


#Verdadero, los modelos de computación especifican las operaciones que se pueden hacer en un algoritmo,
#así mismo nos especifican cuanto tiempo nos va a costar estas operaciones para sumarlas y saber el tiempo 
#que nos costara el algoritmo


# ### 3.  La búsqueda en un árbol binario de búsqueda es siempre mas rápida que la búsqueda lineal en un arreglo

# In[ ]:


#Falso, no siempre es mas rapida, depende de los prerequisitos para la busqueda binaria.


# ### 4. Un algoritmo de complejidad O(nlog(n)) es mas rápido que un algoritmo de complejidad O(n) 

# In[ ]:


#Falso, complejidad lineal siempre va a ser mas rápida que complejidad casi lineal.
#O(n) < O(n log n)


# ### 5.  Un algoritmo de complejidad Ω(nlog(n)) es mas rápido que un algoritmo de complejidad Ω(n)

# In[ ]:


#Falso, complejidad lineal siempre va a ser mas rápida que complejidad casi lineal.
#Ω(n) < Ω(n log n)


# ## Problemas de programación
# #### Todo el código debe ser en Python. Si se requiere escribir funciones que hagan búsqueda o ordenamiento (search, sort), programe las funciones usando los conceptos aprendidos en clase. No use las funciones que Python provee para hacer esto. 

# ### 6. Dada una lista enlazada que represente un número. Por ejemplo, 123 es representado por la lista 1->2->3 si la lista es simple o con doble enlace si es doble. Escriba un programa que haga lo siguiente:
# 
# 1. Reciba dos números A y B como input
# 
# 2. Transforme estos números a listas enlazadas como la definida arriba
# 
# 3. Implemente la resta de los números descritos por esas listas enlazadas. El resultado (A-B) debe ser almacenado en una lista enlazada.
# 
# 4. Imprima el resultado concatenando el valor de los nodos de la lista enlazada resultante
# 
# Nota: asuma que el número A es mayor que B

# In[6]:


class node:
    def _init_(self, data = None, next = None):
        self.data = data
        self.next = next

class linked_list: 
    def _init_(self):
        self.head = None
    
    def add_end(self, data):
        if not self.head:
            self.head = node(data = data)
            return
        aux = self.head
        while aux.next:
            aux = aux.next
        aux.next = node(data = data)
    
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, end =" -> ")
            node = node.next
        print("\n")

linked_listA = linked_list()
linked_listB = linked_list()
linked_listC = linked_list()

A = input('Digite numero (A): ')
B = input('Digite numero (B): ')

valorA = int(A)
valorB = int(B)
valorC = str(valorA - valorB)

for i in list(A):
    linked_listA.add_end(i)
    
for j in list(B):
    linked_listB.add_end(j)  

for k in list(valorC):
    linked_listC.add_end(k)

linked_listA.print_list()
linked_listB.print_list()
linked_listC.print_list()


# ### 7.  Cuando introducimos el concepto de pilas (stacks), usamos como ejemplos una pila de platos. Siguiendo con el ejemplo, una pila de platos con muchos platos se puede caer. Para evitar esto, se puede empezar una nueva pila.
# 
# Implemente una clase de Python que defina un arreglo de stacks. La idea de tener este arreglo es que cuando un stack alcance su capacidad máxima, un nuevo stack empieza en el mismo arreglo. Las operación pop() debe retornar el mismo valor que lo haría si estuviéramos usando un stack simple. 
# 
# Nota: Debe definir los elementos de la clase: el arreglo de stacks, la capacidad del arreglo (# de stacks en el arreglo), la capacidad de cada stack (# de elementos que puede tener el stack). 
# 
# Hint: Cuando ingrese elementos (push), los elementos van al stack que este activo (el stack que recibe y retira elementos). Debe manejar las condiciones para cambiar el stack activo (cuando un push() deja al stack sin elementos, o cuando un pop() llena el stack).

# In[ ]:


class Arreglo_de_Stacks (x):
    
    def __init__(self, n):
        self.total_count: int=0
        self.n : int=num
        self.index : int=0
        self.stacks_en_arreglo = self.crear(self.n)
        
    def lleno(self):
        if self.total_count is self.n:
            raise ValueError("Capacidad maxima alcanzada")
        
    def crear (self,n):
        return [Stack(n)] * n
    
    def push_Arreglo(self, item):
        lleno(self)
        print("Elementos actuales: ", +str(self.stacks_en_arreglo[self.index].item_count))
        if self.stacks_en_arreglo[self.index].item_count is self.num:
            self.index += 1
            self.stack_en_arreglo[self.index].itemcount = 0


# ### 8. Dada una cola con prioridad (PriorityQueue) que contiene elementos (k,v) donde k define la prioridad y v define el valor. Recuerde que los valores con menor k tienen mayor prioridad, es decir si tenemos dos elementos (k1, v1) y (k2, v2), v2 tiene preferencia para salir de la cola antes que v1 si k2< k1. Definimos algunas de las operaciones como siguen:
# 
# ```
# import ctypes
# 
# class PriorityQueue(object):
# 
# """
# 
# Implementation of the queue data structure
# 
# """
# 
# def __init__(self, n):
# 
# self.item_count = 0
# 
# self.n = n
# 
# self.queue = self._create_queue(self.n)
# 
# def _create_queue(self, n):
# 
# """
# 
# Creates a new stack of capacity n
# 
# """
# 
# return (n * ctypes.py_object)()
# 
# def dequeue(self):
# 
# """
# 
# Remove an element from the queue
# 
# """
# 
# c = self.queue[0]
# 
# for i in range(1,self.item_count):
# 
# self.queue[i-1] = self.queue[i]
# 
# self.queue[self.item_count - 1] = ctypes.py_object
# 
# self.item_count -= 1
# 
# return c
# ```
# 
# ### Implemente los métodos enqueue y decreaseKey, tal que ambos métodos tengan complejidad O(log(n)), sin utilizar funciones nativas de Python. Por ejemplo, si necesita hacer una búsqueda, no use la función de Python que implementa esto, programe la función usando for o while loops.

# In[7]:


def enqueue(self,v,k):
    new_node = Node(v,k)
        
    if self.tail == None:
        self.head = self.tail = new_node

    elif v < self.head.priority:
        new_node.next = self.head
        self.head = new_node

    elif v >= self.tail.priority:
        self.tail.next = new_node
        self.tail = new_node

    else:
        temp = self.head.next
        pretemp = self.head
        while v > temp.priority:
            pretemp = temp
            temp = temp.next
        pretemp.next = new_node
        new_node.next = temp
        
def decreaseKey(self, v, s, k):
    if s == k:
        if self[s] > v:
            return s
        else:
            return s+1
        
    if s > k:
        return s
  
    mid = (s+k)/2
    
    if self[mid] < v:
        return decreaseKey(self, v, mid+1, k)
    
    elif self[mid] > v:
        return decreaseKey(self, v, s, mid-1)


# ### 9. Tenemos un árbol binario (binary tree), definimos a un nodo X como rojo, si todos los nodos en el recorrido de la raiz al nodo X tienen un valor que es menor o igual a X. Por ejemplo, en el ejemplo de abajo:
# 
# ![](./binary_tree.png)
# 
# El recorrido hacia el nodo 3 de la izquierda es 3 → 1 → 3, como todos los valores en este recorrido son menores o iguales a 3 (3=3 y 1<3), el nodo es rojo. Similarmente, en el sub-árbol de la derecha, los nodos 4 y 5 también son rojos. Escriba una función en Python que cuente el numero total de nodos rojos. El input de esta función es la raíz del árbol binario.
# 
#  

# In[14]:


def __init__(self, val = 0, left = None, right = None):
    self.val = x
    self.left = None
    self.right = None
    nodo.right = None
    nodo.left = None

def red(self, root):
    conteo = 0
    if self.root == None:
        return False
    total = []
    stack_de_nodos = []
    stack_de_nodos.append(self.root)
    while (len(stack_de_nodos) > 0):
        nodo = stack_de_nodos.pop()
        if nodo.val <= stack_de_nodos[0].val
            conteo += 1
            total.append(node.val)
        if node.right:
            stack_de_nodos.append(nodo.right)
        if node.left:
            stack_de_nodos.append(nodo.left)
    return conteo  


# In[ ]:




