def sangnt():
    prime =[True for i in range(1000000)]
    prime[0] = False
    prime[1] = False
    p=2
    while(p*p <1000000):
        if(prime[p] == True):
            for i in range(p ** 2,1000000,p):
                prime[i] = False
        p+=1
    
    return prime
[n,x] = [int(a) for a in input().split()]
prime=sangnt()
list=[]
list.append(x)
count=0
for j in range(2,1000000):
    if(prime[j]):   
        list.append(list[count]+j)
        count+=1
    if(count==n):
        break

for i in list :
    print(str(i)+" ",end='')