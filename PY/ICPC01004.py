

t = int(input())
while (t > 0):
    a = []
    s = input()
    s=s+'a'
    str=""
    for i in s :
        if(i<= '9' and i >='0') :
            str = str + i
        else :
            if(str != '') :
                a.append(int(str))
            str=''
    min_ = a[0]
    for x in a :
        if( x > min_) : min_ = x
    print(min_)
    t = t-1

    