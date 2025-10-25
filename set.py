#set {}>>> collection of objects
#output will not in order


# set={"umar",8,9.0,676,"o"}
# print(type(set))
# print(set)

# set1={}
# print(type(set1)) # if we dont give any value to set then this will be dictionary type data

# # can use loop to access
# for i in set:
#     print(i)
    
    
# #set methods
a={1,2,3,4}
b={4,5,6,7}

# union    collect all item and neglect same
# print(a.union(b))


# #update   it will update the set with other set means add other set in the update  set
# # a.update(b)  #now it add value of b in set a
# # print(a)


# #intersection >> same items
# print(b.intersection(a))  


#update same as in union but accordig to operation means same
# a.intersection_update(b)
# print(a)  #now its update value by perfoming intersection


#symmetric diff 
#add two sets and neglect common or same values in both
# print(a.symmetric_difference(b))
# print(a)

# #difference it will remove same items 
# a.difference(b)
# print(a)


#isdisjoint >>>no common values in both set
print(a.isdisjoint(b))  #false because there is same


#superset >>> such as a is super set of means "is all value of b is found in a "
print(a.issuperset(b))  #false bcz there in not all value of b is present in a


#subset >>> opposite of super subset means "is b is found in a"
print(a.isdisjoint(b))


#add >> add a new data in set
a.add(91)
print(a)

#remove/discard>>>delete any value inside the set 
#if value not present inside the func remove>>will give error but discard not give error
a.remove(91)
print(a)
a.discard(728372)  #if we use remove it will give error
print(a)


#pop give any one random value inside the set
print(a.pop())


#clear >>>delete data inside the set but not dlete set means it will clear the set

# del delete entire set 
del a
print(a) #will give error bcz we delete it  


