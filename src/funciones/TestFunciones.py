'''
Created on 4 oct 2024

@author: carlo
'''


#Funcion 1
def funcion1(n:int,k:int):
        s = 1
        for i in range(k+1):
            s = s * (n - i + 1)
        return s



if __name__ == '__main__':
    n=3
    k= 4
    if n>k:
        
        print(f"El resultado del producto es: {funcion1(n,k)}")
        
    else:
        print('El numero n tienes que ser mayor que k ')
        
        
   
    