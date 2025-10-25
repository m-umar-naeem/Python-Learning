#to add value in strings >string formating
#we know string printrs as it is but if we want to add variable value or any expresseion we use it
#f keyword use before qoutes
a="Umar"
b=18
print(f"My name is {a} and age is {b}")

pie =3.14151617
print(f"{pie:.2f}")  #this method used to print 2 value after point







#doc strings
# used to view comments inside the functions
#we can access comments type by ._doc_

def pr(a):
    '''MY NAME IS UMAR'''#we can accecs this comment line by doc
    return a+a
    
print(pr.__doc__)    #it will print as it is comments