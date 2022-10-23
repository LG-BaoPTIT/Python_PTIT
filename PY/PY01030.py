def ucln(a, b) :
    if(b == 0) :
        return a
    return ucln(b,a % b)

a,n = map(int, input().split())
d = int(0)
for i in range(pow(10,n-1), pow(10,n)):
    
    if(ucln(a,i) == 1) :
       
        if(d % 10 ==0) : print('')
        d = d + 1
        print(i, end = ' ')
    
