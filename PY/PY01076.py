def ucln(a,b):
    if(b==0):
        return a
    return ucln(b,a%b)

t = int(input())
while(t>0):
    a=int(input())
    b=int(input())
    print(ucln(a, b))
    t-=1