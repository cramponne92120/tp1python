i = int(input())
j = int(input())

s=0
while(i!=0):
    if(i%2):
        s = s + j
    i = i//2
    j=j+j
print(s)