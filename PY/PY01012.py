s1=input()
s2=input()
n=int(input())
for i in range(len(s1)):
    if(i!=n-1):
        print(str(s1[i]),end='')
    else :
        print(str(s2),end='')
        break
for j in range(n-1,len(s1)) :
    print(str(s1[j]),end='')