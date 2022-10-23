def check(s) :
    
    for i in range(0, len(s)) :
        if (i%2 == 0 and n[i] != n[0]) :
            return False
        if (i%2 == 1 and n[i] != n[1]) :
            return False
    return True

t = int(input())
while(t > 0) :

    n = input()
    if(check(n)) : print("YES")
    else : print("NO")
    t = t - 1