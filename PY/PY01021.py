t = int(input())
while(t>0):
    sum=0
    t-=1
    l = list(input())
    l2=[]
    for i in range(len(l)) :
        if(l[i]>='0' and l[i]<='9') :
            sum +=int(l[i])
        else :
            l2.append(l[i])   
    l2.sort()
    print(''.join(l2)+str(sum))      
        