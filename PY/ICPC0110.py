t = int(input())
while(t>0):
    t-=1
    n = int(input())
    list=[]
    list = [int(x) for x in input().split()]
    sum=0
    for i in range(3) :
        sum += max(list)
        list.remove(max(list))
    print(sum)