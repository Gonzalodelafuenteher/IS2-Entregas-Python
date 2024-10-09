'''
Created on 4 oct 2024

@author: carlo
'''
import math

#Funcion 1
def funcion1(n:int,k:int):
        s = 1
        for i in range(k+1):
            s = s * (n - i + 1)
        return s

#funcion 2

def funcion2(a1:int,r:int,k:int):
    var_producto:int = 1
    for n in range(k+1):
        an = a1 * ( r ** ( n-1 ) )
        var_producto = var_producto * an
    return var_producto




#funcion3 
def funcion3(n,k):  
    if n>=k:
        return  math.factorial(n)/((math.factorial(k))*(math.factorial(n-k)))


#funcion4



if __name__ == '__main__':
        n=5
        k= 4
        if n>k:
            
            print(f"El resultado del producto es: {funcion1(n,k)}")
            
        else:
            print('El numero n tienes que ser mayor que k ')
        ################
        a1 = 2
        r = 2
        k2= 4
        
        print( funcion2 (a1,r,k2))
        
        #################
        n1 = 5
        k3 = 2
        print (funcion3(n1,k3))
        
        #################
        
    