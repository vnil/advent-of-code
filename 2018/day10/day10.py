from collections import defaultdict
import re
import math


def draw(arr):
    minX = min([k['x'] for k in arr])
    maxX = max([k['x'] for k in arr])
    minY = min([k['y'] for k in arr])
    maxY = max([k['y'] for k in arr])
    # p = [0] * (maxY-minY + 1)
    d = defaultdict(dict)

    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            d[y][x] = '.'

    for o in arr:
        d[o['y']][o['x']] = 'X'

    for y in range(minY, maxY + 1):
        stri = ''
        for x in range(minX, maxX + 1):
            stri += d.get(y, None).get(x, None)
        print(stri)


regex = r"(-?\d+)"

arr = []
i = 0
for line in open('./day10.txt').readlines():
    res = re.findall(regex, line)
    res = [int(k) for k in res]
    obj = {'x': res[0], 'y': res[1], 'vx': res[2], 'vy': res[3]}
    arr.append(obj)


for q in range(50000):

    maxY = -9999999
    minY = 99999999
    for item in arr:
        x = item['x']+item['vx']
        y = item['y']+item['vy']
        minY = min(minY, y)
        maxY = max(maxY, y)
        item['x'] = x
        item['y'] = y
    if (maxY - minY <= 10):
        draw(arr)
        print(q)
        exit(0)
