
import math


def gen_primes(n):
    primes = []
    a = int(math.sqrt(n))+1
    for x in range(n+1):
        ok = True
        for test in range(2, a):
            if x % test == 0 and x != test:
                ok = False
                break
        if ok:
            primes.append(x)
    return primes


primes = gen_primes(10000)

house = 1
while True:
    current = house
    comb = []
    pointer = 0
    s = int(math.sqrt(house)) + 1
    while primes[pointer] < s:
        if current % primes[pointer] == 0:
            current = current // primes[pointer]
            comb.append(primes[pointer])
            if current == 1:
                break
        else:
            pointer+=1
    
    