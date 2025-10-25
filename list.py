# list[] starting from 0 index like array
#can store diff types of data
# access by negative and positive index
#starting from zero[0] and if we start from ending we use [-1] ,2nd last [-2] so on
#mutable >>>>>>>> we can change value after initilization

#------------------------------

# l=[1,0,"umarr",True,complex(2,3)]
# print(l[1])   #[1]=0 becz 2nd element is 0
# print(l[-1])
# print(l[-5])


a=[0,10284,4,4,6.87,2,4,8]
print(a[-1])  
print(a[0:]) #starting from zero to end
print(a[0::2])#use this if we start from 0 but not know ending and want only even value
print(a[0::4]) #skip  3 and print every 4th values

#to generate lsit with loop for int 
lis=[i for i in range(5)]
print(lis)  # now it will print from 0-4 due to index



lis=[i*i for i in range(5)] 
print(lis)  # now it will print from 0-4(squares) due to index

lis=[i*i for i in range(5) if i==4] #we can aslo add condition so it print only when codition is true
print(lis)


# LIST METHODS

a=[1,2,3,4,5,6]

# 1-append =====>ad value at the end
a.append(6)
print(a)


#2-sort  >>> change to order >>minimum to maimum
b=[4,7,9,1,5,61]
b.sort()
print(b)
#and if we want to max to min
b.sort(reverse=True)
print(b)


# 3-reverse  reverse all values
c=[1,2,4,5,6]
c.reverse()
print(c)


#4index  give the index where value is stored
d=[1,2,3]
print(d.index(1))  #1 is stored at 0 index


# 5-count homw many time used in stored data
e=[1,2,3,41,1,1,3,1]
print(e.count(1))


# copy >>>>copy all value to another var and can change by other var
f=[12,11,3,4,5,7,8]
l=f.copy()
l[0]=11
print(l)


#insert >>> it is uses to insert value at any index where we want
g=[1,2,3,4,5]
g.insert(5, 6) #such as we want to add 6 at index 5
print(g)


#extend >>> add new variablue values to exist variable
h=[11,22,44]
h.extend(g)
print(h)   #now its extend h and add values of g at end


#concatenate >> add values 
print(g+h) #>>>add value of h in g






