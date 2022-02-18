a = int(input())
o = 0
i=0
while(a != 1):
    if(a%2 == 0):
        o = a//2
    else:
        o = 3*a+1
    print(o,"\n")
    a = o
    i+=1
print(i)
