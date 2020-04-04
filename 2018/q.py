def in_range(s, e, vs, ve):
    return s < ve and vs < e


def conflict(timeSlot, ev):
    for j in timeSlot:
        if in_range(j[0], j[1], ev[0], ev[1]):
            return True
    return False


def process(ev):
    time_slot_C = []
    time_slot_J = []
    seq = []
    for i in ev:
        if not conflict(time_slot_C, i):
            time_slot_C.append(i)
            seq.append("C")
        elif not conflict(time_slot_J, i):
            time_slot_J.append(i)
            seq.append("J")
        else:
            return 'IMPOSSIBLE'
    return ''.join(seq)


t = int(input())
for i in range(0, t):
    num_of_event = int(input())
    events = []
    for j in range(num_of_event):
        ui = input().split(" ")
        events.append([int(ui[0]), int(ui[1])])
    print("Case #{}: {}".format(i+1, process(events)))

"""
4
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440
"""
