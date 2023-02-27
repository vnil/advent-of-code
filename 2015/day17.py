data = sorted([
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
    3
], reverse=True)


def go(data):
    # combinations = []
    s = set()

    def yo(acc, arr):
        if sum(acc) > 150:
            return
        if sum(acc) == 150:
            # combinations.append(acc)
            s.add(''.join(map(str, sorted(acc))))
            print(len(s))
            return
        for i, _ in enumerate(arr):

            new_arr = arr[:]
            item = new_arr.pop(i)
            new_acc = acc[:]
            new_acc.append(item)
            yo(new_acc, new_arr)

    yo([], data)
    return len(s)


print(go(data))
