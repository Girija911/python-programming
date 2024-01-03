a=int(input())
b=int(input())
for i in range(1,a):
    x=0
    for j in range(2,i):
        if(i%j==0):
            x=x+1
    if(x==0):
        print(i)
        
