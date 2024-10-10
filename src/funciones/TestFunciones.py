'''
Created on 4 oct 2024

@author: carlo
'''
import math

#Funcion 1
def funcion1(n:int,k:int):
        s = 1
        for i in range(k):
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
def funcion3(n:int,k:int):  
    if n>=k:
        return  math.factorial(n)/((math.factorial(k))*(math.factorial(n-k)))
    else:
        print("el valor de n tiene que ser mayor que el de k")


#funcion4
def funcion4(n,k):
    if n>=k: 
        primera = 1/math.factorial(k)
        sumatorio = 0 
        for i in range(0,k):
            var_sumatorio = ((-1)**i) * funcion3(k+1, i+1) * (k-i)**n
            sumatorio = sumatorio + var_sumatorio
        return primera * sumatorio 
    else:
        print("n tiene que ser mayor que k")  
#funcion5



if __name__ == '__main__':
        n=4
        k= 2
        if n>k:
            
            print(f"El resultado del producto es: {funcion1(n,k)}")
            
        else:
            print('El numero n tienes que ser mayor que k ')
        ################
        a1 = 2
        r = 2
        k2= 2
        
        print( funcion2 (a1,r,k2))
        
        #################
        n1 = 4
        k3 = 2
        print (funcion3(n1,k3))
        
        #################
        n2 = 4
        k4 = 1
        
        print(funcion4(n2,k4))
    