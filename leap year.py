date=input()
x=date.split("/")
year = int(x[2])
if(year%4==0):
    print(year,"is a leap year")
elif(year%100==0):
    print(year,"is not a leap year")
elif(year%400==0):
    print(year,"is a leap year")
if(year%4!=0):
    x=year%4
    print(year-x)
else:
    print(year+4)
