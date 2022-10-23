import math
def check(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True

t = int(input())
while(t>0):
    n=input()
    s=""
    for i in range(len(n)-4,len(n)):
        s=s+n[i]
    if(check(int(s))):print("YES")
    else : print("NO")
    t=t-1