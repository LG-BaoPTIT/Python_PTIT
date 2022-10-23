n = int(input())
l = list(map(int, input().split()))
b = 1 
while b: 
    b = 0 
    i=0 
    while(i<len(l)-1): 
        if (l[i] + l[i + 1]) % 2 == 0: 
            del l[i] 
            del l[i] 
            b = 1 
        i+=1 
    i=0 
print(len(l))
