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


monkeys = {
    0: {
        'items': deque([79, 98]),
        'operation': lambda old: old * 19,
        'test': lambda val: 2 if val % 23 == 0 else 3,
        'inspection': 0
    },
    1: {
        'items': deque([54, 65, 75, 74]),
        'operation': lambda old: old + 6,
        'test': lambda val: 2 if val % 19 == 0 else 0,
        'inspection': 0
    },
    2: {
        'items': deque([79, 60, 97]),
        'operation': lambda old: old * old,
        'test': lambda val: 1 if val % 13 == 0 else 3,
        'inspection': 0
    },
    3: {
        'items': deque([74]),
        'operation': lambda old: old + 3,
        'test': lambda val: 0 if val % 17 == 0 else 1,
        'inspection': 0
    }
}

# 96577
monkeys = {
    0: {
        'items': deque([84, 72, 58, 51]),
        'operation': lambda old: old * 3,
        'test': lambda val: 1 if val % 13 == 0 else 7,
        'inspection': 0
    },
    1: {
        'items': deque([88, 58, 58]),
        'operation': lambda old: old + 8,
        'test': lambda val: 7 if val % 2 == 0 else 5,
        'inspection': 0
    },
    2: {
         'items': deque([93, 82, 71, 77, 83, 53, 71, 89]),
         'operation': lambda old: old * old,
         'test': lambda val: 3 if val % 7 == 0 else 4,
        'inspection': 0
    },
    3: {
         'items': deque([81, 68, 65, 81, 73, 77, 96]),
         'operation': lambda old: old + 2,
         'test': lambda val: 4 if val % 17 == 0 else 6,
        'inspection': 0
    },
    4: {
         'items': deque([75, 80, 50, 73, 88]),
         'operation': lambda old: old + 3,
         'test': lambda val: 6 if val % 5 == 0 else 0,
        'inspection': 0
    },
    5: {
         'items': deque([59, 72, 99, 87, 91, 81]),
         'operation': lambda old: old * 17,
         'test': lambda val: 2 if val % 11 == 0 else 3,
        'inspection': 0
    },
    6: {
         'items': deque([86, 69]),
         'operation': lambda old: old + 6,
         'test': lambda val: 1 if val % 3 == 0 else 0,
        'inspection': 0
    },
    7: {
         'items': deque([91]),
         'operation': lambda old: old + 1,
         'test': lambda val: 2 if val % 19 == 0 else 5,
        'inspection': 0
    }
}


seen = set()


change = [0] * len(monkeys.values())
prev = [0] * len(monkeys.values())

for round in range(10000):
    for monkey_index in range(len(monkeys.values())):
        monkey = monkeys[monkey_index]
            
        while len(monkey['items']) > 0:
            
            
            worry_level = monkey['items'].popleft()
            worry_level = monkey['operation'](worry_level)% 9699690
                

            next_monkey = monkey['test'](worry_level) 

            monkeys[next_monkey]['items'].append(worry_level)
            #pp(monkeys)
            monkey['inspection']+=1
    
    


inspections = []

for monkey_index in range(len(monkeys.values())):
    inspections.append(monkeys[monkey_index]['inspection'])
pp(inspections)

inspections.sort()
pp(inspections[-1] * inspections[-2])
#14398560027

