t = int(input())
while(t>0):
    n=input()
    d=0
    for i in n:
        if(i>'2') :
            print("NO")
            d=1
            break
    if(d==0) : print("YES")
    t = t-1