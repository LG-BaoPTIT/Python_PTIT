def check_(a,x):
    if(len(a)<3) : return False
    for i in range(1,x+1):
        if(a[i]<=a[i-1]): return False

    for i in range(x+2,len(a)):
        if(a[i]>=a[i-1]): return False

    return True
t = int(input())
while(t>0):
    a = input()
    x=0
    for i in range(1,len(a)-1) :
        if(a[i]>a[i-1] and a[i]>a[i+1]) : x=i
    if(check_(a,x)): print("YES")
    else : print("NO")
    t = t-1