from numpy import intp
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
        if(check_(int(n[i]))):
            k+=1
    if(check_(len(n)) and k > (len(n)-k)):
        print("YES")
    else :
        print("NO")
        
    
