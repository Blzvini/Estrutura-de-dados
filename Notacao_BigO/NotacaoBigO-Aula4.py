# %%

""" 
Exemplos de Big-O

Constant - O(1)


Linear - O(n)

Quadratic - O(n^2) - polynomial

Combination
"""

#Constant 

lista = [1,2,3,4,5]

def constant(n):
    print(n[0])

constant(lista)
    
    
#Linerar

def linear(n):
    for i in n:
        print(i)
        
linear(lista)

# %%

#Quadratic

def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print('-----')
        
quadratic(lista)
# %%

#Combination

# #O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n) -> O(n)
def combination(n):
    #O(1)
    print(n[0])
    
    #O(5)
    for i in range(5):
        print('test', i)
    
    #O(n)
    for i in n:
        print(i)
    #O(n)    
    for i in n:
        print(i)
    
    #O(3)
    for i in n:
        print('Python')
    for i in n:
        print('Python')
    for i in n:
        print('Python')


combination(lista)
# %%
