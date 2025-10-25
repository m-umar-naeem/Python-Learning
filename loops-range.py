x="UMAR"
for umar in x:
    print(umar)
    if umar=='M':
        print("🥰")

list1=["app","soft"]
for io in list1:
    print(io)
    for ok in io:
        print(ok)
        
# range is used to specify range it is start from 0
for i in range(5):
    print(i)
    print(i+1) #if startring from 1
      
for i in range(5,90):   #according to range
    print(i)
    
for i in range(2,20,2): #2 means starting from 2 , 20 means end with 20, and last 2 means gap of 2 for each value between 2-20
    print(i)
    
i =int(input("ENTER"))
while i<=5:
    i=int(input('enter;'))
    print(i)