# imp keyword 
#use in strings for different operations


a='my name is umar'

print(a.upper)
print(a.lower)



#rstrip 
#removing word or character or space from th end such as we
#which word we enter in the rstrip it remove all from left such as it will remove all "m"from b
b="umar-naeemmmmmmmmmmmmmmm"
c="umar-naeem-----------"

print(b.rstrip("m"))
print(c.rstrip("-"))


#replace 
#it will replace word which we enter in replace
print(b.replace("umar","muhammad"))  # now first it will find word and remove all and add new which we enter

# split
# it will split data into "", or in which we want , we enter a word which we want to split with other
#it split when we add space in stored data
print(b.split())  # no spliting
d="i am umar"
print(d.split())
print(d.split("ok well")) #now it will split each space with insert data


#capatilze
#chanfge first word to capital
e="umar"
print(e.capitalize())

#center
#it will cnetrlized the data by parameter means where we want to set
print(e.center(30))
print(e.center(100))

#count
#it will count the word or letter how many time it is used in string etc
f="i will coming"
print(f.count("i"))
print(f.count("w"))

#endwith
#it is used to identify tha the data is ended with this char,num etc or not 
#it will give true if it is en with provide num/dig/str.......
g="i am fine!"
print(f.endswith("!"))  #false
print(g.endswith("!"))  #true

#find/index is same index will give error if word not found and find will give -1 
#it will find the word or letter in index form
#if word exist double it will only find first not others
h="This is my this is not you"
print(h.find("this"))  #it will give index where is stored
print(h.find("you"))
print(h.find("is")) # it will find word with in word means in "this" it will find "is" in it if it is firstly
print(h.find("at"))
# print(h.index("at"))


# isalnum
# to check the str is alphabte and numeric or not
i="ok"
print(h.isalnum())  #false bcz we use spaces
print(i.isalnum())  #true

#isalpha
#to check the str is alphabetic 
print(h.isalpha())   #false we use space
print(i.isalpha())      #true

# islower
# to check  if all data in str is lower case or not
print(h.islower())
print(i.islower())

#isprintable
#to check that all data in str is printable means no specatial or keyword is used
print(h.isprintable())
j="ok\n"
print(j.isprintable())

#swap
#lower to capital and cap to low
print(j.swapcase())

#title 
#capatilze each 1st word
k="ok no go"
print(k.title( ))