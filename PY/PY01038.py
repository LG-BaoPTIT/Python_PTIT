from re import S


def check(n) :
    if(n % 7 ==0) : return n
    for i in range(1000) :
        a = list(reversed(str(n)))
        b = ''.join(a)
        c = int(b)
        n = n + c
        if(n % 7 ==0):
            return n
    return -1
t = int(input())
while(t > 0) :
    n = int(input())
    print(check(n))
    t = t - 1