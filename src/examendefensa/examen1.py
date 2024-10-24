'''
Created on 24 oct 2024

@author: carlo
'''
import math
from math import comb


def P2(n: int, k: int, i: int = 1) -> int:
    assert n >= 0, "n debe ser un número entero positivo"
    assert k >= 0, "k debe ser un número entero positivo"
    assert i >= 0, "i debe ser un número entero positivo"
    assert i < k + 1, "i debe ser menor que k + 1"

    p: int = 1
   
    if k - 2 > 0:
        for j in range(i, k-1):  
            p *= (n - j + 1)
    
    return p


#######################################


def C2(n: int, k: int) -> int:
    
    assert n > 0, "n debe ser un número entero positivo"
    assert k >= 0, "k debe ser un número entero positivo"
    assert n > k, "n debe ser mayor que k"
    
    return math.factorial(n)/((math.factorial(k+1))*(math.factorial(n-k-1)))


def S2(n: int, k: int) -> float:
   
    assert n > 0, "n debe ser un número entero positivo."
    assert k > 0, "k debe ser un número entero positivo."
    assert n >= k, "El valor de n debe ser mayor o igual que k."
    arriba = 1 / math.factorial(k)
    abajo = math.factorial(k + 2)

    sumatorio = 0
    for i in range(k + 1):
        var_sumatorio = (-1) ** i * math.comb(k, i) * (k - i) ** (n + 1)
        sumatorio += var_sumatorio 
    S2_value = (arriba / (n * abajo)) * sumatorio
    return S2_value



def palabrasMasComunes(fichero: str, n: int = 5) -> list[tuple[str, int]]:
    assert n > 1, "n debe ser mayor que 1."
    
    with open(fichero, encoding='UTF-8') as f:
        contador = {}  
        for linea in f:
            for p in linea.split():  
                p = p.strip().lower()  
                if p: 
                    if p in contador:
                        contador[p] += 1
                    else:
                        contador[p] = 1
    
    palabras_comunes = []
    for _ in range(n):
        palabramax = None
        contadormax = 0
        for palabra, count in contador.items():
            if count > contadormax:
                contadormax = count
                palabramax = palabra

        if palabramax is not None:
            palabras_comunes.append((palabramax, contadormax))
            del contador[palabramax]  

    return palabras_comunes


if __name__ == '__main__':
    n = 2
    k = 2
  
    print(P2(n,k))
    
print ("########################################") 

n1 = 6
k1 = 3  
print(C2(n1,k1)) 

    
print ("########################################") 

n2 = 5
k2 = 3

print(S2(n1,k1)) 

print ("########################################") 

resultado = palabrasMasComunes('../../'  + "Resources/archivo_palabras.txt", n=5)
print(resultado)
