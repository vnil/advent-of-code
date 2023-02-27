# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy
import math
import sys

filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]

tail_x = 0
tail_y = 4

D = {
    'D': (0, 1),
    'U': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}

rope = [(tail_x, tail_y)] * 10

visited = set([(tail_x, tail_y)])

for row in content:
    direction, right = row.split()
    steps = int(right)
    dx, dy = D[direction]
    print(direction, steps)
    for _ in range(steps):
        rope[0] = (rope[0][0] + dx, rope[0][1] + dy)
        for rope_index in range(1, len(rope)):
            head_x, head_y = rope[rope_index - 1]
            tail_x, tail_y = rope[rope_index]
            if abs(head_x - tail_x) >= 1 or abs(head_y - tail_y) >= 1:
                # Update tail
                if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
                    continue

                if head_y != tail_y and head_x != tail_x:
                    #Diagnol
                    if abs(head_x - tail_x) > 1 and abs(head_y - tail_y) > 1:
                        #Fat diagnol
                        tail_y = (head_y + tail_y)//2
                        tail_x = (head_x + tail_x)//2  
                    elif abs(head_y - tail_y) > 1:
                        tail_x = head_x
                    else:
                        tail_y = head_y
                    
                if head_x == tail_x and tail_y != head_y:
                    tail_y = head_y - 1 if head_y > tail_y else head_y + 1
                if head_y == tail_y and tail_x != head_x:
                    tail_x = head_x - 1 if head_x > tail_x else head_x + 1

                rope[rope_index] = (tail_x, tail_y)
            else:
                continue
        visited.add(rope[9])
        print(rope)
                

pp(visited)            
print(len(visited))