#List = changable and ordered
#Set = Unordered and non immutable
#Tuple= non changable ordered

listt=["Coconut","Mango","Papaya","Pomegranate"]

set={"Coconut","Coconut","Mango","Papayaa"}

tuplee=(1,2,3,4,5,2,4,6)

print(set)
listt[0]=3
print(listt)
print(tuplee)

# 2d 

listt=[[1,2,3,4],[1,2,5,6],[8,9,6,4],[2,6,4,5]]

for list in listt:
    for item in list:
        print(item,end="")
    print()

#Dictionories = ordered changable and no duplicates

capitals={"india":"delhi","usa":"washington"}
print(capitals.get("india"))
