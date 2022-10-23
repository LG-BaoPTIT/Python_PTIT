def giaithua(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua

t = int(input())

while(t>0):
    t-=1
    n=input()
    sum=0
    for i in n :
        sum += giaithua(int(i))
        
    if(int(n)==sum):
        print("Yes")
    else :
        print("No")