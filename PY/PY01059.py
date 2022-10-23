t = int(input())
while(t>0):
    t-=1
    n=input()
    tong=0
    tich=1
    d=0
    for i in range(len(n)):
        if(i%2==0):
            if(int(n[i]) != 0):              
                tich = tich * int(n[i])
        else :
            tong += int(n[i])

    print(tich,end='')

    print(" " + str(tong))
