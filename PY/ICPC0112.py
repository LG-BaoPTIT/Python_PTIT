t = int(input())
prime = [True for i in range(1000009)]
prime[0]=prime[1]=False
for g in range(1000):
    if(prime[g]==True):
        for j in range(g*2,1000001,g):
            prime[j]=False

while(t>0) :
    t-=1
    n=int(input())
    x=0
    for i in range(2,n-5):
        if(prime[i] and prime[i+6]):
            if(prime[i+2] or prime[i+4]):
                x+=1
    print(x)

