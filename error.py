#try and expect is keyword used in py for error handling
#error handling means if error occur in program skip this and execute next lines

def ok(a,b):
    return int(a*b)

i=input("enter")    
j=input("enter")

try:
   print(int(i)*int(j))
except:
    print("please enter mul")
    
    

# a=10
# b=input()


# try:
#     print(int(a)/int(b))
# except ValueError:
#     print("erroe")
# except IndexError:
#     print("ok")
    
    

# FINALLY keyword is used to execute always when an error occured or not
#we mostly use this in functions whe we want to print something compulsory
a=input()
b=input()
try:
    print(int(a)/int(b))
except:
    print(a+b)
finally:
    print("your choice")



#raising error
#a method in which we raise a error for future
#such as we should enter num between 0-9 and user enter digites or letters so it will raise error

a=int(input())
if a<0 or a>10:
    raise ValueError("no value")  #now it will raise wroor if user input data more than 9 or any letters etc


    
    
    
    
    