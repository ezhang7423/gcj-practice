# 3
# 4
# 1 2 3 4
# 2 1 4 3
# 3 4 1 2
# 4 3 2 1
# 4
# 2 2 2 2
# 2 3 2 3
# 2 2 2 3
# 2 2 2 2
# 3
# 2 1 3
# 1 3 2
# 1 2 3

'''
1
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
'''


def process(matrix):
    rr = 0
    rc = 0
    tr = 0
    columns = []
    for i in range(len(matrix)):
        columns.append([])
    for i, r in enumerate(matrix):
        if len(set(r)) != len(r):
            rr += 1
        for j, t in enumerate(r):
            columns[j].append(t)
        # print(r, i)
        # print(r[i])
        tr += int(r[i])
    for i in columns:
        if (len(set(i)) != len(i)):
            rc += 1
    return (tr, rr, rc)


t = int(input())
for i in range(0, t):
    rows = int(input())
    matrix = []
    for j in range(rows):
        ui = input().split(" ")
        matrix.append(ui)
    ans = process(matrix)
    print("Case #{}: {} {} {}".format(i+1, ans[0], ans[1], ans[2]))
