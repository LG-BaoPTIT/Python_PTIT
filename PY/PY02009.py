t = int(input())
while(t>0):
    t-=1
    n = int(input())
    list =[]
    dic={}
    while(n>0):
        list.append(int(input()))
        n-=1
    for i in list :
        if str(i) in dic :
            dic[str(i)]+=1
        else:
            dic[str(i)] = 1
    value_dic = sorted(dic.values())
    max_ = value_dic[len(value_dic)-1]
    items_dic = sorted(dic.items())
    for x in items_dic: 
        if(x[1]==max_):
           print(x[0])
           break 
    