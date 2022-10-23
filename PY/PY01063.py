t = int(input())
while(t>0):
    t-=1
    n=list(input())
    x = input()
    count = 0
    for i in range(len(n)-2):
        s=''.join(n[i:i+len(x)])  
        if(s==x):
            count+=1
            for j in range(i,i+len(x)):
                n[j]='a'
            
    
    
    print(count)