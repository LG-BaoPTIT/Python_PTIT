n = input()

l = list(n)
index_ = l.index('.')
s= n[index_+1:len(n)]

if(len(n)<3) :
    print('no')
else : 
    if(s.lower()=="py"):
        print('yes')
    else :
        print('no')
    