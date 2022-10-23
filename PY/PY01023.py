import math


t = int(input())
while(t>0):
    n=int(input())
    h=n
    print("1 * ",end='')
    for i in range(2,h+1,1) :
        
        if(n%i==0):
            x = 0
            while(n%i==0) :
                n=n/i
                x = x+1
            if(n!=1):
                print(str(i)+'^'+str(x)+" * ",end='')
            else :
                print(str(i)+'^'+str(x),end='')  
    print('')      

    t = t-1