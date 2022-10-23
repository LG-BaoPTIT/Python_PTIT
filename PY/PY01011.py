def check(c):
    if(len(c) % 2 == 1) : return 0
    for i in c :
        if(int(i) % 2 ==1) : return 0
    return 1


t = int(input())
while(t > 0) :
    a = input()    
    for i in range(10, int(a), 2) :
       
        b = list(reversed(str(i)))
        c = ''.join(b) 
        if(str(i) == c and check(str(i))) :
            print(i, end = " ")
    print("")
    t = t - 1