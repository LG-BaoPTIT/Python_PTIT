t= int(input())
while(t>0):
    t-=1
    n=input()
    list1 = [int(x) for x in input().split()]
    list2 = [int(x) for x in input().split()]
    list1.sort()
    list2.sort()
    d=0
    for i in range(int(n)) :
        if(list1[i]>list2[i]):
            d=1
    if(d==1):
        print("NO")
    else :
        print("YES")