

def add(char, num):
    return ''.join([char for x in range(num)])


def balance(raw):
    ans = []
    l = 0
    for x in list(raw):
        num = int(x)
        if l == num:
            ans.append(x)
        if l > num:
            ans.append(add(')', l - num))
            ans.append(x)
            l -= l - num
        if l < num:
            ans.append(add('(', num - l))
            ans.append(x)
            l += num - l
    if l > 0:
        ans.append(add(')', l))
    return ''.join(ans)


t = int(input())
for i in range(1, t + 1):
    raw = input()
    ans = balance(raw)
    print("Case #{}: {}".format(i, ans))


'''
4
0000
101
111000
1
'''
