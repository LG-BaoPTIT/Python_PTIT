t = int(input())
while(t>0):
    t-=1
    n = int(input())
    str = input()
    list=[]
    dic={}
    for o in str.split():
        list.append(o)
    
    
    for i in list :
        if i in dic :
            dic[i]+=1
        else:
            dic[i] = 1
    value_dic = sorted(dic.values())
    max_ = value_dic[len(value_dic)-1]
    items_dic = sorted(dic.items())
    d=0
    for x in items_dic: 
        if(x[1]==max_ and max_ > int(n/2)):
           print(x[0])
           d=1
           break 
    if(d==0):
        print("NO")