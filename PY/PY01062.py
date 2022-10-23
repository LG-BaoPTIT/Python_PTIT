def check(a):
    if(a<2): return False
    for i in range(2,a):
        if(a%i==0): return False
    return True
t =int(input())
while(t>0):
    t-=1
    n = input()
    count_ = 0
    for i in range(len(n)):
        if(check(int(n[i]))):
            count_+=1
    if(check(len(n)) and count_ > len(n) - count_):
        print("YES")
    else :
        print("NO")
