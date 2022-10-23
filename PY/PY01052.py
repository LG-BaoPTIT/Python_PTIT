def check_(h):
    if(h<2): return False
    for i in range(2,h) :
        if(h%i==0) : return False
    return True

#main
t = int(input())
while(t>0) :
    t-=1
    n = input()
    k=0
    for i in range(len(n)) :       
        k+=int(n[i])
    if(check_(k) ):
        print("YES")
    else :
        print("NO")
        
    
