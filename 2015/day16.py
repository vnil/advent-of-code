containers = [
11,
30,
47,
31,
32,
36,
3,
1,
5,
3,
32,
36,
15,
11,
46,
26,
28,
1,
19,
3]

containers = [20, 15, 10, 5, 5]


count = 0
dp = set()

def rec(arr, left, used):
    global count
    if left == 0:
        used.sort()
        if tuple(used) not in dp:
            print(left, used)
            dp.add(tuple(used))
            count+=1
        return
    elif left < 0 or len(arr) == 0:
        return
    copy = arr.copy()
    for i, item in enumerate(copy):
        rec(arr, left - item)
        arr.insert(i, item)



rec(containers, 25, [])
print(count)