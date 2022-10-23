def solve(n, s):
    if len(s) % n != 0:
        for i in range(n - len(s) % n):
            s = '0' + s
    res = ''
    token = 0
    for i in range(len(s)):
        token += int(s[i]) * 2 ** (n - 1 - i % n)
        if (i + 1) % n == 0:
            if token == 10:
                res += 'A'
            elif token == 11:
                res += 'B'
            elif token == 12:
                res += 'C'
            elif token == 13:
                res += 'D'
            elif token == 14:
                res += 'E'
            elif token == 15:
                res += 'F'
            else : res += str(token)
            token = 0
    return res
# main
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if n == 2:
        n = 1
    elif n == 4:
        n = 2
    elif n == 8:
        n = 3
    else:
        n = 4
    s = solve(n, input())
    print(s)