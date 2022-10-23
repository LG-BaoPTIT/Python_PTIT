t = 10

set_={}
list=[]
sum =0
while(t>0):
    data = input()
    
    for i in data.split():
        list.append(i)
    t = t - len(data.split())

set_ ={int(x)%42 for x in list}    
print(len(set_))