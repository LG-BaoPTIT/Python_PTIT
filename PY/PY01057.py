import math
def prime(s):
    if s<2: return False
    for i in range(2,int(math.sqrt(s))+1):
        if s%i==0: return False
    return True

def check(s):
    for i in range(len(s)):
        if prime(i) and s[i]!='2' and s[i]!='3' and s[i]!='5' and s[i]!='7':
            return False
        if prime(i)==False and (s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i]=='7'):
            return False
    return True

t=int(input())
for i in range(t):
    s=input()
    if check(s): print("YES")
    else: print("NO")