
def check(a):
    if(a<2): return False
    for i in range(2,a):
        if(a%i==0): return False
    return True
t = int(input())
while(t>0):
    t-=1
    n =input()
    s1=n[0:3]
    s2=n[len(n)-3:len(n)+1]
    if(check(int(s1)) and check(int(s2))):
        print("YES")
    else :
        print("NO")