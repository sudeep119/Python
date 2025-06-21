temp=44
raining=True

if temp>35 or temp<10 or raining:
    print("Match is cancelled")
    
temp=36
sunny =True
if temp>=35 and sunny:
    print("It is hot outside")
elif temp<=34 and not sunny:
    print("Normal weather")