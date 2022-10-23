t = int(input())

while ( t> 0) :
    a,b=map(str, input().split())
    if(int(a) > int(b)) :
        c = b
        b = a
        a = c
    
   
    x=list(input())
    y=list(input())
    for i in range(0,len(x)) :
        if(x[i] == b) :x[i] = a 
    for i in range(0,len(y)) :
        if(y[i]== b) :y[i] = a
    print(int(str(''.join(x))) + int(str(''.join(y))),end=' ')
    for i in range(0,len(x)) :
        if(x[i] == a) :x[i] = b 
    for i in range(0,len(y)) :
        if(y[i]== a) :y[i] = b
    print(int(str(''.join(x))) + int(str(''.join(y))))
    t = t -1