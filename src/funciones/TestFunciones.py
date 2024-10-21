'''
Created on 21 oct 2024

@author: carlo
'''
from funciones.Funciones import funcion1, funcion2, funcion3, funcion4 , funcion5


if __name__ == '__main__':
    
        print ('################################################')
        print("TEST DE LA FUNCION 1: ")
        n:int = 4
        k:int = 2
        if n>k:
            
            print(f"El producto de {n} y {k} es: {funcion1(n,k)} \n")
            
        else:
            print('El numero n tienes que ser mayor que k ')

        print ('################################################')
        print("TEST DE LA FUNCION 2: ")
        
        a1:int = 3
        r:int = 5
        k2:int= 2
        
        print(f"El producto de la secuencia geométrica con a1 = {a1}, r = {r} y k = {k2} es: {funcion2 (a1,r,k2)} \n")
        
        print ('################################################')
        print("TEST DE LA FUNCION 3: ")
    
        n1:int = 4
        k3:int = 2
        print (f"El producto de {n1} y {k3} es: {funcion3(n1,k3)} \n")
        
        print ('################################################')
        print("TEST DE LA FUNCION 4: ")
        
        n2 = 4
        k4 = 2
        
        print(f"El número S(n,k) siendo n = {n2} y k = {k4} es: {funcion4(n2,k4)} \n")
        
        print ('################################################')
        print("TEST DE LA FUNCION 5: ")
        a:float = 3
        epsilon:float= 0.001
        f = lambda x: 2*x**2
        fd = lambda x: 4*x
        print(f"Resultado de la función 5 con a = {a} y e = {epsilon},  f(x) = 2x^2 y f'(x) = 4x  : {funcion5(epsilon, f, fd,a)} \n")
    