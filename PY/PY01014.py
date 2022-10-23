
a, k, n= [int(x) for x in input().split()]
b=k-a%k
check=False
s=""
for i in range(b,n+1-a,k):
    check=True
    s+=str(i)+" "
if check==False: print("-1")
else: print(s)


