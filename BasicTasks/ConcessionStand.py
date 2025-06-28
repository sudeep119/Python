listt={"pizza":3.50,"coconut":2.45,"apple":1.50,"ginger":0.5}

for item,price in listt.items():
    print(f"{item} {price}")
    
cart=[]
total=0

while True:
    food=input("Enter the food (q to quit)")
    if food=='q':
        break
    if listt.get(food) is not None:
        cart.append(food)
   
for item in cart:
    total+=listt.get(item)
    
print(cart) 
print(total)