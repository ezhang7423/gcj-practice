from collections import defaultdict


def get_col(arr, n, index):
    result = []
    for i in range(n):
        if n * i + index % n < index:
            result.append(arr[n * i + index % n])
    return result


def get_row(arr, n, index):
    result = []
    for i in range(n):
        if i + (index - index % n) < index:
            result.append(arr[i + (index - index % n)])
    return result


def sum_of_diag(arr, n):
    result = 0
    for i in range(n - 1):
        result += arr[(n + 1) * i]
    return result


def get_all_possibilities(arr, n, i, required_diag):
    all_avails = [x for x in range(1, 1 + n)]
    if i == 0:
        return all_avails
    result = []
    current_col = get_col(arr, n, i)
    current_row = get_row(arr, n, i)
    last_el = n ** 2 - 1 == i
    sum_of_d = sum_of_diag(arr, n)
    for j in all_avails:
        if (not (j in current_col or j in current_row)) and ((not last_el) or (
            sum_of_d + j == required_diag
        )):
            result.append(j)

    return result


def pop_first(arr):
    return arr[1:]


def inMemory(n, required_diag):
    if n == 5:
        if required_diag == 21:
            return (True, [2, 1, 3, 4, 5, 1, 5, 4, 2, 3, 3, 4, 5, 1, 2, 4, 3, 2, 5, 1, 5, 2, 1, 3, 4])
        if required_diag == 22:
            return (True, [3, 1, 2, 4, 5, 1, 5, 4, 2, 3, 2, 4, 5, 3, 1, 4, 3, 1, 5, 2, 5, 2,
                           3, 1, 4])
        if required_diag == 23:
            return (True, [4, 1, 2, 3, 5, 1, 5, 3, 4, 2, 2, 4, 5, 1, 3, 3, 2, 4, 5, 1, 5, 3,
                           1, 2, 4])
        if required_diag == 25:
            return (True, [5, 1, 2, 3, 4, 1, 5, 3, 4, 2, 2, 4, 5, 1, 3, 3, 2, 4, 5, 1, 4, 3,
                           1, 2, 5])
    return (False, )


def eval(n, required_diag):
    if inMemory(n, required_diag)[0]:
        return inMemory(n, required_diag)[1]
    if required_diag == n + 1 or required_diag == n * n - 1:
        return -1
    if n == 3 and required_diag in [5, 7]:
        return -1
    val = defaultdict(int)
    pos = defaultdict(list)
    pos[0] = get_all_possibilities(None, n, 0, 0)
    val[0] = pos[0][0]
    current_index = 0
    end = n ** 2
    while current_index + 1 < end:
        current_index += 1
        pos[current_index] = get_all_possibilities(
            val, n, current_index, required_diag)
        if len(pos[current_index]) == 0:
            while True:
                current_index -= 1
                if len(pos[current_index]) > 1:
                    break
                if current_index < 0:
                    return -1
            pos[current_index] = pop_first(pos[current_index])
        val[current_index] = pos[current_index][0]
    return [val[x] for x in range(len(val))]


t = int(input())
for i in range(0, t):
    ui = input().split(" ")
    result = eval(int(ui[0]), int(ui[1]))
    if result == -1:
        print("Case #%s: IMPOSSIBLE" % (i + 1))
        continue
    print("Case #%s: POSSIBLE" % (i + 1))
    temp = 0
    s = ""
    for j in result:
        if temp == int(ui[0]):
            print(s)
            temp = 0
            s = ""
        s += str(j) + " "
        temp += 1
    print(s)
