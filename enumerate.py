# enumerate
#a function which has already index of values stored in list ,tupple or str
#such as we have a condition we want to print a message or value at specific index we can use it 
#bcz it  stored index already
a=[2,3,5,6,8,9,4,2,1,5,5,6,10]
for index,a in enumerate(a):
    print(a)
    if index==2:
        print("3rd value") #now it will print this message after index 3
        
        #we use it for short
        
        
#if we want to show index also we use it
b=[2,3,5,6,8,9,4,2,1,5,5,6,10]

for index,b in enumerate(b):
    print(index,b) #now it will show index with value
    
    
# we can also start index from 1
c=[2,3,5,6,8,9,4,2,1,5,5,6,10]

for index,c in enumerate(c,start=1):  #now it will start with 1
    print(index,c)