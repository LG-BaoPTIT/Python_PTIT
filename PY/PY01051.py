t= int(input())
while(t>0):
    t-=1
    n = input()
    sum=0
    for i in range(len(n)) :
        sum += int(n[i])
    org_str = str(sum)
    new_str_list = list(org_str)
    new_str_list.reverse()
    new_str = ''.join(new_str_list)
    if(int(new_str)==sum and sum>10):
        print("YES")
    else :
        print("NO")
