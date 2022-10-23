def kiemtra(a, b) :
    for i in range(1,len(a)) : 
        if(abs(ord(a[i])-ord(a[i-1])) != abs(ord(b[i])-ord(b[i-1]))): 
            return 0
    
    return 1    

t = int(input())
while(t>0) :
    a = input()
    b = list(reversed(a))
    if(kiemtra(a,b) == 1): print("YES")
    else : print("NO")
    t = t-1

