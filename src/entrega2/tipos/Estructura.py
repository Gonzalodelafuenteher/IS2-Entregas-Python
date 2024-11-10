'''
Created on 10 nov 2024

@author: gonza
'''
from typing import List, TypeVar, Generic, Callable, Tuple
from abc import ABC, abstractmethod

# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')

class Agregado_lineal(ABC, Generic[E]):
    """
    Clase base para los objetos agregados lineales.
    """

    def __init__(self):
        # Inicializa una lista vacía para almacenar elementos
        self._elements: List[E] = []

    def size(self) -> int:
        """
        Devuelve el número de elementos en la colección.
        :return: Int
        """
        return len(self._elements)

    def is_empty(self) -> bool:
        """
        Verifica si la colección está vacía.
        :return: Boolean
        """
        return self.size() == 0

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos.
        :return: List
        """
        return self._elements.copy()
    
    @abstractmethod
    def add(self, e: E) -> None:
        """
        Agrega un elemento a la colección.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        raise NotImplementedError("Método abstracto: debe ser implementado en la subclase.")

    def add_all(self, ls: List[E]) -> None:
        """
        Agrega todos los elementos de una lista a la colección.
        :param ls: Lista a agregar
        :raise NotImplementedError: Método abstracto
        """
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        return self._elements.pop(0)
    # Aqui lo que hace es borrar el primer elemento, mira si la lista esta vacia 
    # y so no lo esta borra el primero 
    
    def remove_all(self) -> List[E]:
        """
        Elimina todos los elementos de la colección.
        :return: Lista eliminada
        """
        removed_elements = self._elements.copy()
        self._elements.clear()
        return removed_elements



class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        # Inicializa la colección con una función de ordenación
        super().__init__()
        self._order = order

    @classmethod
    def of(cls, order: Callable[[E], R]) -> 'Lista_ordenada[E, R]':
        """
        Crea una instancia de la clase lista ordenada.
        :param order: Función de ordenación
        :return: Instancia de Lista_ordenada
        """
    
        return cls(order)

    def __index_order(self, e: E) -> int:
        assert len(self._elements) > 0, "La lista está vacía."
    
        if e < self._elements[0]:  # Cambiado de () a []
            return 0
    
        if e > self._elements[len(self._elements) - 1]:  # Cambiado de () a []
            return len(self._elements)
    
        for i in range(len(self._elements)):  # Cambiado de len(self._elements) a range(len(self._elements))
            if e < self._elements[i]:  # Cambiado de elements(i) a _elements[i]
                return i
    
        return len(self._elements)  # Si no se encuentra un índice, se retorna el tamaño de la lista
        
    # Acceso a la lista: Cambié self._elements(0) y self._elements(len(self._elements)) a self._elements[0] y self._elements[len(self._elements) - 1], respectivamente.
    #Iteración sobre la lista: Cambié for i in len(self._elements): a for i in range(len(self._elements)): para iterar correctamente sobre los índices de la lista.
    #Acceso a elementos: Cambié self.elements(i) a self._elements[i] para acceder a los elementos de la lista.  
         
    # Aqui lo que hacemo es unicamente el proceso de ordenar el numero 

    def add(self, e: E) -> None:
        
        posicion = self.__index_order(e)
        self._elements.insert(posicion, e)
        
    # Lo que hace esta funcion es coger la funcion de ordenar y la utiliza con ese numero,
    # entonces ya sabe donde poner el numero y con la funcion insert metemos el numero en su sitio
    
    def __str__(self)->str:
       
        return "ListaOrdenada(" + ", ".join(str(e) for e in self._elements) + ")"
    
    



class Lista_ordenada_sin_repeticion(Lista_ordenada[E, R], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        # Inicializa la colección con una función de ordenación
        super().__init__()
        self._order = order
        
    @classmethod
    def of(cls, order: Callable[[E], R]) -> 'Lista_ordenada_sin_repeticion[E, R]':
        """
        Crea una instancia de la clase lista ordenada.
        :param order: Función de ordenación
        :return: Instancia de Lista_ordenada
        """
        return cls(order)
    
    def add(self, e: E) -> None:
        cont = 0
        
        for i in len(self._elements):
            if e == self._elements(i):
                cont += cont
        if cont < 1:
            posicion = self.__index_order(e)
            self._elements.insert(posicion, e)
            
            
    def __index_order(self, e: E) -> int:
        assert len(self._elements) > 0, "La lista está vacía."
        if e < self._elements[0]:  # Cambiado de () a []
            return 0
    
        if e > self._elements[len(self._elements) - 1]:  # Cambiado de () a []
            return len(self._elements)
    
        for i in range(len(self._elements)):  # Cambiado de len(self._elements) a range(len(self._elements))
            if e < self._elements[i]:  # Cambiado de elements(i) a _elements[i]
                return i
    
        return len(self._elements)  # Si no se encuentra un índice, se retorna el tamaño de la lista
        
    # Acceso a la lista: Cambié self._elements(0) y self._elements(len(self._elements)) a self._elements[0] y self._elements[len(self._elements) - 1], respectivamente.
    #Iteración sobre la lista: Cambié for i in len(self._elements): a for i in range(len(self._elements)): para iterar correctamente sobre los índices de la lista.
    #Acceso a elementos: Cambié self.elements(i) a self._elements[i] para acceder a los elementos de la lista.  
         
    # Aqui lo que hacemo es unicamente el proceso de ordenar el numero 
    
    def __str__(self)->str:
       
        return "Lista_ordenada_sin_repeticion(" + ", ".join(str(e) for e in self._elements) + ")" 
      



class Cola(Agregado_lineal[E]):
    @classmethod
    def of(cls) -> 'Cola[E]':
        return cls()

    def add(self, e: E) -> None:
        self._elements.append(e) 
        """
        Agrega un elemento a la cola.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
    def __str__(self)->str:
       
        return "Cola(" + ", ".join(str(e) for e in self._elements) + ")"  
   
        



class Cola_prioridad(Generic[E, P]):
    def __init__(self):
        # Inicializa dos listas vacías, una para los elementos y otra para sus prioridades
        super().__init__()
        self._prioridad: List[E] = []

    def size(self) -> int:
        """
        Devuelve el número de elementos en la colección.
        :return: Int
        """
        return len(self._elements)

    def is_empty(self) -> bool:
        if len(self._elements) == 0:
            return True
        else:
            return False

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos de mayor a menor prioridad
        :return: List
        """
        return self._elements.copy()

    def add(self, e: E, priority: P) -> None:
        """
        Agrega un elemento y sus prioridades a la cola.
        :param e: Elemento a agregar
        :param priority: Prioridad del elemento
        """
        index = self.index_order(priority)
        self._elements.insert(index, e)
        self._prioridad.insert(index, priority)
        


    def remove(self) -> E:
        """
        Elimina el primer elemento de la cola. El primer elemento es el de mayor prioridad.
        :return: Elemento eliminado
        :raise IndexError: Si la cola está vacía
        """
        assert not self.is_empty(), 'El agregado está vacío'
        self._prioridad.pop(0)  
        return self._elements.pop(0)
   
    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())
        return removed_elements
    
    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        """
        Agrega todos los elementos y sus prioridades a la cola.
        :param ls: Lista de tuplas (elemento, prioridad, )
        """
        for e, prioridad in ls:
            self.add(e, prioridad)
    

    def decrease_priority(self, e: E, new_priority: P) -> None:
        """
        Reduce la prioridad del elemento en la cola. El elemento debe estar en la cola, y la nueva prioridad debe ser menor
        :param e: Elemento a reducir prioridad.
        :param new_priority: Prioridad nueva para el elemento
        """
        if e in self._elements:
            index = self._elements.index(e)
            current_priority = self._priorities[index]
            if new_priority < current_priority: 
                self.remove()  
                self.add(e, new_priority)  
      

    def __repr__(self) -> str:
        return "ColaDePrioridad[" + ", ".join(f"({e}, {p})" for e, p in zip(self._elements, self._priorities)) + "]"


class Pila(Agregado_lineal[E]):
    """
    Una Pila es una estructura de datos que sigue el principio LIFO (Last In, First Out).
    Los elementos se apilan y solo se puede acceder al elemento en la parte superior.
    
    IMPORTANTE. Como la estructura subyacente es una lista, la parte superior de la pila es el primer 
    elemento de la lista.
    """
    
    def add(self, element: E) -> None:
        """Añade un nuevo elemento a la parte superior de la pila (al principio)."""
        self.elements.insert(0, element)  # Inserta el elemento al principio de la lista


    @classmethod
    def of(cls) -> 'Pila[E]':
        """Método de fábrica que crea e inicializa una nueva instancia de la clase."""
        return cls()