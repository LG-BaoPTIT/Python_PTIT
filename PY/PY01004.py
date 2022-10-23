def ucln(a,b) :
    if(b==0):
        return a
    return ucln(b,a%b)
def check_(k):
    if(k<2): return False
    for i in range(2,k) :
        if(k%i==0) : return False
    return True

#main
t = int(input())
while(t>0) :
    t-=1
    k=0
    n = int(input())
    for i in range(1,n):
        if(ucln(i,n)==1 ):
            k+=1
    if(check_(k)):
        print("YES")
    else :
        print("NO")
