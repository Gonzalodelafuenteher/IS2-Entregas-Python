'''
Created on 19 dic 2024

@author: carlo
'''
from typing import Dict, Set, Optional
from entrega3.grafo.recorridos import *
from entrega3.grafo.grafon import *
class Gen:
    
    def __init__(self, nombre: str, tipo: str, num_mutaciones: int, cromosoma: str):
        
        self.nombre = nombre
        self.tipo = tipo
        self.num_mutaciones = num_mutaciones
        self.cromosoma = cromosoma

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, cromosoma: str) -> "Gen":
        
        return Gen(nombre, tipo, num_mutaciones, cromosoma)

    @staticmethod
    def parse(linea: str) -> "Gen":
        
        partes = linea.strip().split(",")  
        if len(partes) != 4:
            raise ValueError(f"La línea no tiene el formato esperado: {linea}")
        
        nombre = partes[0]
        tipo = partes[1]
        num_mutaciones = int(partes[2])
        cromosoma = partes[3]
        
        return Gen(nombre, tipo, num_mutaciones, cromosoma)

    def __repr__(self) -> str:
        
        return f"{self.nombre}, {self.tipo}, {self.num_mutaciones}, {self.cromosoma})"
    
###################################################################################################################
    
class RelacionGenAGen:
        
        def __init__(self, nombre_gen1: str, nombre_gen2: str, conexion: float):
           
            if not (-1 <= conexion <= 1):
                raise ValueError(f"El valor de conexión debe estar entre -1 y 1, no {conexion}.")
            self.nombre_gen1 = nombre_gen1
            self.nombre_gen2 = nombre_gen2
            self.conexion = conexion
    
        @staticmethod
        def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> "RelacionGenAGen":
            
            return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)
    
        @staticmethod
        def parse(linea: str) -> "RelacionGenAGen":
           
            partes = linea.strip().split(",")  # Dividir la línea por comas
            if len(partes) != 3:
                raise ValueError(f"La línea no tiene el formato esperado: {linea}")
            
            nombre_gen1 = partes[0]
            nombre_gen2 = partes[1]
            try:
                conexion = float(partes[2])
            except ValueError:
                raise ValueError(f"El valor de conexión no es un número válido: {partes[2]}")
    
            return RelacionGenAGen.of(nombre_gen1, nombre_gen2, conexion)
    
        @property
        def coexpresados(self) -> bool:
           
            return self.conexion > 0.75
    
        @property
        def antiexpresados(self) -> bool:
            
            return self.conexion < -0.75
    
        def __repr__(self) -> str:
            
            return (f"RelacionGenAGen({self.nombre_gen1}, {self.nombre_gen2}, "
                    f"conexion={self.conexion:.2f})")
        
#########################################################################################################

    

class RedGenica(Grafo[str, float]):
   
    def __init__(self, es_dirigido: bool = True, adyacencias: Dict[str, Dict[str, float]] = {}) -> None:
        super().__init__(es_dirigido, adyacencias)
        self.genes_por_nombre: Dict[str, Gen] = {}

    @staticmethod
    def of(es_dirigido: bool = True) -> "RedGenica":
       
        return RedGenica(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = True) -> "RedGenica":
        
        red_genica = RedGenica.of(es_dirigido)

        
        with open(f1, 'r') as archivo_genes:
            for linea in archivo_genes:
                gen = Gen.parse(linea.strip())
                red_genica.add_vertex(gen.nombre)
                red_genica.genes_por_nombre[gen.nombre] = gen

        
        with open(f2, 'r') as archivo_relaciones:
            for linea in archivo_relaciones:
                relacion = RelacionGenAGen.parse(linea.strip())
                if relacion.nombre_gen1 not in red_genica.genes_por_nombre or \
                   relacion.nombre_gen2 not in red_genica.genes_por_nombre:
                    raise ValueError(f"Uno de los genes en la relación no existe: {linea.strip()}")

                red_genica.add_edge(relacion.nombre_gen1, relacion.nombre_gen2, relacion.conexion)

        return red_genica

    def get_gen(self, nombre: str) -> Optional["Gen"]:
        
        return self.genes_por_nombre.get(nombre)

    def get_relaciones(self, nombre: str) -> Dict[str, float]:
        
        return self.adyacencias.get(nombre, {})

    def mostrar_red(self) -> None:
        
        print("Genes:")
        for gen in self.genes_por_nombre.values():
            print(gen)

        print("\nRelaciones:")
        for origen, destinos in self.adyacencias.items():
            for destino, peso in destinos.items():
                print(f"{origen} -> {destino} [peso={peso}]")



if __name__ == "__main__":

    genes_file = "genes.txt"
    red_genes_file = "red_genes.txt"
    red_genica = RedGenica.parse(genes_file, red_genes_file, es_dirigido=False)
    camino = dfs(red_genica, 'KRAS', 'PIK3CA')
    g_camino = red_genica.subgraph(camino)
    g_camino.draw("caminos", lambda_vertice=lambda v: v, lambda_arista=lambda e: e)

    print("El camino más corto desde 'KRAS' hasta 'PIK3CA' es:")
    
    

    