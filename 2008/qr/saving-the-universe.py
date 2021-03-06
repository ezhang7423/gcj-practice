import copy
inpu = '''2
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol
'''


def isInt(s):
    try:
        null = int(s)
        return True
    except ValueError:
        return False


with open('A-small-practice.in', 'r') as fin:
    raw = fin.read().splitlines()
cases = raw.pop(0)

totalSwitches = []
for x in range(int(cases)):
    totalSwitches.append(0)
    searchEngines = {}
    for y in range(int(raw.pop(0))):
        searchEngines[raw.pop(0)] = 0
    y = 0
    if (raw.pop(0) == '0'):
        continue
    while True:
        tmpSearch = copy.deepcopy(searchEngines)
        if len(raw) == 0 or isInt(raw[0]):
            break
        while len(raw) != 0 and len(tmpSearch.keys()) != 0 and not isInt(raw[0]):
            tmpSearch.pop(raw.pop(0), None)
            y += 1
        totalSwitches[x] += 1
    totalSwitches[x] -= 1

with open('Ab.out', 'w') as fout:
    for i, x in enumerate(totalSwitches):
        fout.write('Case #'+str(i+1)+': '+str(x)+'\n')
print(totalSwitches)
