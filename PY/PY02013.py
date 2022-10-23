n = int(input())
count=1
while( n!= 0):
    
    if(n==1):
        print(count)
        n=int(input())
        count=1
    else:
        if(n%2==0) :
            n=n/2
            count+=1
        else:
            n=n*3+1
            count+=1
    


