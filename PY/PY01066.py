import math
def check(str,new_str):
    for i in range(len(str)-1):
        if(abs(ord(str[i+1])-ord(str[i])) != abs(ord(new_str[i+1])-ord(new_str[i]))) :
            return False
    return True        


t = int(input())
while(t>0):
    t-=1
    str = input()
    s = list(str)
    s.reverse()
    new_str = ''.join(s)
    
    if(check(str,new_str)):
        print("YES")
    else : print("NO")