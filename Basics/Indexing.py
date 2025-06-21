str="Helloo World!"

print(str[0])
print(str[-1])
print(str[0:4])
#rev ind
print(str[-4:-1])
#reverse
print(str[::-1])
print(str[0::2])

#format specifiers
#{value:flags}
#decimal formatting
price1=12.2424
print(f"Formated number is {price1:.2f}")
#space 
print(f"Formated number is {price1:10}")
#zero filling
print(f"Formated number is {price1:010}")
#left justify
print(f"Formated number is {price1:<10}")
#right justify
print(f"Formated number is {price1:>10}")
# + if pos same for - if neg
print(f"Formated number is {price1:+}")
# , for 1000s values and more 