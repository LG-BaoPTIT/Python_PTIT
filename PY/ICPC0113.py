from cgi import print_arguments


t = int(input())

while(t>0):
    t-=1
    n=int(input())
    prime = [True for i in range(1000009)]
    prime[0]=prime[1]=False
    for g in range(1000):
        if(prime[g]==True):
            for j in range(g*2,1000001,g):
                prime[j]=False
    for i in range(10,n):
        org_str =str(i)
        new_str_list = list(org_str)
        new_str_list.reverse()
        new_str = ''.join(new_str_list)       
        
        x=int(new_str)
        if(prime[i] and prime[x] and i!=x and x<n) :
            print(i,end='')  
            print(" ",end='')
            print(x,end='')
            print(" ",end='')
            prime[i] = False
            prime[x] = False
            
    print('')

