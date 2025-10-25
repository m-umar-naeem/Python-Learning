def inti(x,y):
    summ=x+y
    print(summ)
    div=x/y
    print(div)
    mull=x*y
    print(mull)
    
a=int(input("enter"))
b=int(input("enter"))
print(inti(a,b))
def str(umar,naem):
    print(umar,naem)
    
print(str('s','m'))
str("U","N")

# functions fror tupple
def tupp(*n):
    sum=0
    for i in n:
        sum=i+sum
    # print("av",sum/len(n))
    return sum/len(n)
        
print(tupp(8,8,9,0,3) )