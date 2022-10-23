P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while( True) :
    str = input()
    if(str == '0') : break 
    n,s = str.split()
    g=''
    for i in s : 
        g = g + P[(P.index(i) + int(n)) % 28]
        
    print(''.join(list(reversed(g))))   
