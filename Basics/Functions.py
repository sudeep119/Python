#positional function
def hello(name):
    print(f"Helloo world {name}")

hello("Sudeep")
hello("Broo")

#default

def fullname(first,last=" "):
    return first+" "+last

print(fullname("Sudeep","K S"))
print(fullname("Sudeep"))
# Key word 

def fullnames(first,middle,last):
    return first+" "+middle+" "+last

name=fullnames(middle="K",first="Sudeep",last="S")

print(name)

#Arbitary

#*args allows you to pass multiple non-key argument
# **kwargs allows you to pass multiple keyword-arguments

def names(*args):
    print(type(args))
    for arg in args:
        print(arg+" ",end="")
        
names("Sudeep","k","s")

def address(**kwargs):
    for key,val in kwargs.items():
        print(f"{key } {val}")
    
address(house_no=12,street="Hosamane",area="Hosmne")