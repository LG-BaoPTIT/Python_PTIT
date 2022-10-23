from itertools import count


t = int(input())

while(t>0) :
    t=t-1
    n,d = [int(x) for x in input().split()]
    list=[]
    list = [int(y) for y in input().split()]
    x=d%n
    for i in range (x,n):
        print(list[i],end='')
        print(" ",end='')
    for i in range (0,x):
        print(list[i],end='')
        print(" ",end='')
    print('')