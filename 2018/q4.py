

def sym(f, b):
    if f == list(reversed(b)):
        return 'sym'
    elif f == [1 if x == 0 else 0 for x in list(reversed(b))]:
        return 'opp'
    else:
        return 'reg'


def firstBitdiff(f, b):
    l = len(b) - 1
    for i, x in enumerate(f):
        if x != b[l - i]:
            return i


def firstBitSim(f, b):
    l = len(b) - 1
    for i, x in enumerate(f):
        if x == b[l - i]:
            return i


def findSwitch(f, b):
    mode = sym(f, b)
    print('1')
    new1 = int(input())
    if mode == 'sym':
        print('1')
        new1 = int(input())
        if f[0] == b[len(b)-1]:
            tr = ['fl', 'ne']
        else:
            tr = ['ne', 'fl']
        if f[0] != new1:
            return tr[0]
        else:

            return tr[1]
    elif mode == 'opp':
        print('1')
        new1 = int(input())
        if f[0] == b[len(b)-1]:
            tr = ['ne', 'fl']
        else:
            tr = ['fl', 'ne']
        if f[0] != new1:

            return tr[0]
        else:

            return tr[1]
    else:
        if f[0] == b[len(b)-1]:
            i = firstBitdiff(f, b)
            print(str(i + 1))
            newD = int(input())
            if f[0] != new1:
                # possibilites left are both and flip
                if newD == f[i]:
                    return 'bo'
                else:
                    return 'fl'
            else:
                # possibilites are reverse and neither
                if newD == f[i]:
                    return 'ne'
                else:
                    return 'rev'
        else:
            i = firstBitSim(f, b)
            print(str(i + 1))
            newD = int(input())
            if f[0] != new1:
                if newD == f[i]:
                    return 'rev'
                else:
                    return 'fl'
            else:
                # both or neither
                if newD == f[i]:
                    return 'ne'
                else:
                    return 'bo'


def reverse(front, back):
    return [back[::-1], front[::-1]]


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


def writeans(front, back, bitlen):
    sol = [str(x) for x in front] + [' ' for x in range(bitlen -
                                                        2 * len(front))] + [str(x) for x in back]


def solve(bitlen):
    front = []
    back = []
    for x in range(5):
        print(x + 1)
        front.append(int(input()))
    for x in range(5):
        print(bitlen - x)
        back.insert(0, int(input()))
    writeans(front, back, bitlen)
    while (len(front + back) != bitlen):
        # do some check if over
        switch = findSwitch(front, back)
        if switch != 'ne':
        if switch == 'fl':
            front, back = flip(front, back)
            front, back, done = findNew(front, back, bitlen)
        elif switch == 'rev':
            front, back = reverse(front, back)
            front, back, done = findNew(front, back, bitlen)
        elif switch == 'bo':
            front, back = flip(front, back)
            front, back = reverse(front, back)
            front, back, done = findNew(front, back, bitlen)
        elif switch == 'ne':
            front, back, done = findNew(front, back, bitlen)
        writeans(front, back, bitlen)
        if done:
            break
    sol = [str(x) for x in front + back]
    print(''.join(sol))


t, b = [int(a) for a in input().split(' ')]
for i in range(1, t+1):
    solve(b)
    if (input() != 'Y'):
        break
