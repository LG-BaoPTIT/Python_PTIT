from cgi import print_arguments



t = int(input())
prime = [True for i in range(10000009)]
prime[0]=prime[1]=False
for g in range(10000):
    if(prime[g]==True):
        for j in range(g*2,10000009,g):
            prime[j]=False
while(t>0):
    t-=1
    n=int(input())
   
    org_str =str(n)
    new_str_list = list(org_str)
    new_str_list.reverse()
    new_str = ''.join(new_str_list) 
    x=int(new_str)     
    sum_=0
    d=0
    for i in range(len(org_str)):
        if(prime[int(org_str[i])]==False) :
            d=1
            break
    
    if(prime[i] and prime[x] and d==0) :
        print("Yes")
    else : 
        print("No")
            
    

