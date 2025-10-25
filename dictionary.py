# it give keys to access vales 
dic = {
#"kety":"value"
"name" : "umar",
"age": 19,
"class":13

    
}
print(dic["name"])
print(dic["age"])


dic2={
    1:"umar",
    2:"ok",
    3:"oo"
}
print(dic2[2])  #if the data is not found in the dicionary it will not give error

#we can also access data by .get keyword

print(dic2.get(1))  # it will not give error


#keys 
#if we want to print all keys we use this it will print keys inly not values
print(dic2.keys())


#print by for loop
for i in dic2:
    print(i)  #it will print keys only
    
#values 
#when we want to print values
print(dic2.values())

#it will give items name and values
print(dic2.items())

#this will give key and value in good way 
for key,value in dic2.items():
    print(f"the key is {key} and the val is {value}")
    
    
    
    
# dictionary methods
# update same as we use first
dic3={1:100,
      2:88,
      3:67,
      4:77,
      5:99}
dic3.update({1:90})  #it will update the value of 1 
print(dic3)
dic4={
    6:44,
    7:87
}
dic3.update(dic4)    #now it will update dic3 and add data of dic 4 in dic 3
print(dic3)


#clear same as we use>>clear all data inside dict
dic.clear()
print(dic)

#pop>>it will remve key and value which we want
dic2.pop(1)  #now it will remove the key 1 and its value
print(dic2)

#popitem>>it will remove the last key and its value in the dict
dic2.popitem()
print(dic2)

#del same as
del dic
# print(dic) #now it will give error bcz we delete it
del dic2[2]
print(dic2)



