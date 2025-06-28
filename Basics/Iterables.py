# iterables= an object or collection that can return its element one at a time

items=[1,2,3,4,5]

for item in items:
    print(item,end=" ")
    
items2={1,2,2,3,4,5,5}
for item in items2:
    print(item,end="-")
    
#Membership operators= use to test whether a var is in sequence or not
# in not in

fruits=["mango","coconut","papaya"]

for fruit in fruits:
    print(fruit)

print("hhh" not in fruits)


