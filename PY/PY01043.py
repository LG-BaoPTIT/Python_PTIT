def check(n):
    if(len(n) % 2==1) : return False
    for i in range(0,int(len(n)/2)) :
        if(int(n[i]) % 2==1) :return False
    b = list(n)
    b.reverse()
    str = ''.join(b)
    if(str!=n) : return False
    return True

t = int(input())
while(t>0):
    n=int(input())
    for i in range(22,n,1):
        if(check(str(i))==True): print(str(i) + " ",end='')
    print("")
    t = t-1