def ucln(a,b) :
    if(b == 0) :
        return a
    return ucln(b, a % b)

t = int(input())
while(t > 0) :
    a = input()
    b = list(reversed(a))
    c= ''.join(b)
    if(ucln(int(a), int(c)) == 1 ) : print("YES")
    else : print("NO")
    t = t-1