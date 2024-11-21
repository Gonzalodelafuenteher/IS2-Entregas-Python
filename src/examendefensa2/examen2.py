'''
Created on 21 nov 2024

@author: carlo
'''

from typing import List, TypeVar, Generic, Callable
from abc import ABC, abstractmethod


E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')

class Agregado_lineal(ABC, Generic[E]):
    

    def __init__(self):
       
        self._elements: List[E] = []

    def size(self) -> int:
        
        return len(self._elements)

    def is_empty(self) -> bool:
        
        return self.size() == 0

    def elements(self) -> List[E]:
        
        return self._elements.copy()
    
    @abstractmethod
    def add(self, e: E) -> None:
        
        raise NotImplementedError("Método abstracto: debe ser implementado en la subclase.")

    def add_all(self, ls: List[E]) -> None:
        
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        return self._elements.pop(0)
   
    
    def remove_all(self) -> List[E]:
    
        removed_elements = self._elements.copy()
        self._elements.clear()
        return removed_elements
    
    
    def find(self, func: Callable[[E], bool]) -> E | None:

        for elem in self._elements:
            if func(elem):
                return elem
    
    def contains(self, e: E) -> bool:
        
        return e in self._elements
    
    def filter(self, func: Callable[[E], bool]) -> List[E]:
        res = []  
        for elem in self._elements:
            if func(elem):  
                res.append(elem)  
        return res
    
    


############################################################################################################

class ColaConLimite(Agregado_lineal[E]):
    
    def __init__(self, capacidad: int):
        super().__init__()
        if capacidad <= 0:
            raise ValueError("La capacidad tiene que ser mayor que 0.")
        self.capacidad = capacidad
    
    @classmethod
    def of(cls, capacidad: int) -> "ColaConLimite":
        return cls(capacidad)

    
    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está a tope , no puedes añadir mas ")
        self._elements.append(e)

    def is_full(self) -> bool:
        return self.size() >= self.capacidad
    
    def __repr__(self) -> str:
        return "ColaConLimite[" + ", ".join(str(e) for e in self._elements) + "]"

   


if __name__ == '__main__':
    
    
    print("=== Ejemplo de uso con ColaConLimite ===")
    cola:ColaConLimite= ColaConLimite.of(3)
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")

    
    try:
        cola.add("Tarea 4")  
    except OverflowError as e:
        print(e)  


    print("¿La cola está llena?", cola.is_full())  
    
    print(cola)
    
    print ("##############################################################################################")
    
    cola2: ColaConLimite[int] = ColaConLimite.of(5)

    cola2.add(5)
    cola2.add(7)
    cola2.add(15)
    cola2.add(25)
    
    encontrado_10 = cola2.find(lambda x: x == 10)  
    encontrado_25 = cola2.find(lambda x: x == 25) 
    print(f"Elemento encontrado (10): {encontrado_10}")  
    print(f"Elemento encontrado (25): {encontrado_25}") 
    
    x = 6
    y = 25
    contiene_x: bool = cola2.contains(x)  
    contiene_y: bool = cola2.contains(y)  
    print(f"¿Contiene {x}? {contiene_x}")  
    print(f"¿Contiene {y}? {contiene_y}")  


    mayores_a_10: List[int] = cola2.filter(lambda x: x > 10)  
    print(f"Elementos mayores a 10: {mayores_a_10}")

   
    
    