#Cesar Murillo
#CIS261
#IterationAndRecursion

def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num * factorial_recursive(num-1)

def factorial_iterative(num):
