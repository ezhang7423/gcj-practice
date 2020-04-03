def calcDamage(st):
    charge = 1
    damage = 0
    for x in st:
        if x == 'C':
            charge *= 2
        else:
            damage += charge
    return damage


def findSwaps(tol, st):
    swaps = 0
    d = calcDamage(st)
    while d > tol:
        st = swap(st)
        if st == 'impossible':
            return -1
        else:
            swaps += 1
        d = calcDamage(st)
    return swaps


def swap(st):
    st = st[::-1]
    st = list(st)
    first, second = ['', '']
    for i, x in enumerate(st):
        second = x
        if (first + second == 'SC'):
            tmp = st[i]
            st[i] = st[i-1]
            st[i-1] = tmp
            return ''.join(st)[::-1]
        else:
            print(first + second)
        first = second
    return 'impossible'


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
        # read a list of integers, 2 in this case
    x = input()
    d = int(x.split(' ')[0])
    st = x.split(' ')[1]
    ans = findSwaps(d, st)
    if ans == -1:
        ans = "IMPOSSIBLE"
    print("Case #{}: {}".format(i, ans))
    # check out .format's specification for more formatting options
