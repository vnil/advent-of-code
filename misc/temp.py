import time
from collections import defaultdict
import math
start_time = time.time()




def go(nums):
    d = defaultdict(int)
    if len(nums) <= 1:
        return -1
    nums = sorted(set(nums))
    print(nums)
    for n in nums:
        d[n] += 1
        sqrted = math.sqrt(n)
        while True:
            if sqrted != math.floor(sqrted) or int(sqrted) not in d:
                break
            d[int(sqrted)] += 1
            sqrted = math.sqrt(sqrted)
    print(d)
    res = max(d.values())
    return res if res >= 2 else -1
        

print(go([4,3,6,16,8,2]))

print("--- %s seconds ---" % (time.time() - start_time))
            

# while p2 < len(nums):
#         if nums[p2] == c*c:
#             c = nums[p2]
#             m = max(m, p2-p1)
#             p2+=1
#         else:
#             p1 = p2+1
#             p2 = p2+1
#     return m