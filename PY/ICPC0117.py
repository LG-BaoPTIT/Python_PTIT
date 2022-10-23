t = int(input())
list_ = []
while(t>0):
    
    str =input()

    
    d=1
    for i in range(len(list_)):
        if(str == list_[i]):
            d=0
    if(d==1):
        list_.append(str)
    t-=1
print(len(list_))