def sym(f, b):
    if f == list(reversed(back)):
        return 'sym'
    elif f == ['1' if x == '0' else '0' for x in ''.join(list(reversed(back)))]:
        return 'opp'
    else:
        return 'reg'


def firstBitdiff(f, b):
    l = len(b) - 1
    for i, x in enumerate(f):
        if x != b[l - i]:
            return i


def findSwitch(f, b):

    mode = sym(f, b)
    print('1')
    new1 = int(input())
    if mode == 'sym':

    elif mode == 'opp':

    else:
        i = firstBitdiff(f, b)
        print(str(i + 1))
        newD = int(input())
        if f[0] == b[len(b)-1]:
            if f[0] != new1:
                # possibilites left are both and flip
                if newD == f[i]:
                    return 'bo'
                else:
                    return 'fl'
            else:

    return 'fl'


def reverse(front, back):
    front = list(reversed(front))
    back = list(reversed(back))
    return [back, front]


def flip(front, back):
    return [[1 if x == 0 else 0 for x in front], [1 if x == 0 else 0 for x in back]]


def findNew(front, back, bitlen):
    already = len(front)
    total = 2 * already
    if total + 8 >= bitlen:
        for x in range(bitlen - total):
            print(already + x + 1)
            front.append(int(input()))
        return (front, back, True)
    for x in range(4):
        print(already + x + 1)
        front.append(int(input()))
    for x in range(4):
        print(bitlen - x - already)
        back.insert(0, int(input()))
    return (front, back, False)


def solve(bitlen):
    front = []
    back = []
    for x in range(5):
        print(x + 1)
        front.append(int(input()))
    for x in range(5):
        print(bitlen - x)
        back.insert(0, int(input()))
    while (len(front + back) != bitlen):
        # do some check if over
        switch = findSwitch(front, back)
        if switch == 'fl':
            front, back = flip(front, back)
            front, back = findNew(front, back, bitlen)
        elif switch == 'rev':
            front, back = reverse(front, back)
            front, back = findNew(front, back, bitlen)
        elif switch == 'bo':
            front, back = flip(front, back)
            front, back = reverse(front, back)
            front, back = findNew(front, back, bitlen)
        elif switch == 'ne':
            front, back = findNew(front, back, bitlen)

    sol = [str(x) for x in front + back]
    print(''.join(sol))


t, b = [int(a) for a in input().split(' ')]
for i in range(1, t+1):
    solve(b)
    if (input() != 'Y'):
        break
