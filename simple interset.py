a=int(input("enter the principal amount"))
b=int(input("enter the no.of senior citizens"))
sen_citiz=input("is senior citizen(y/n)")
if sen_citiz=="y":
    rate=12
else:
    rate=10
si=a*b*rate/100
print("intersest",si)
