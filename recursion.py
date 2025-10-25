#recursion >>>>call a funcion inside a function 
#such as for repeaiting or looping
#


def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return  n * fact(n-1)   # we call a function inside a function so it will be continue till conditionh is tru


print(fact(6))



def fab(n):
    if n==0:
        return 0
    else:
        return  (n-1)+(n-2)
    
print(fab(3))
print(fab(5))
