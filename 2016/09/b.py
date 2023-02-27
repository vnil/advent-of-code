import collections

file_content = open('ex', 'r').readlines()
sa = file_content[0]


def expand(s):
    i = 0
    start = None
    l = 0
    while i < len(s):
        c = s[i]
        if c == "(":
            start = i
        elif c == ")":
            a, b = [int(q) for q in s[start+1:i].split('x')]
            sub = s[i+1:a+i+1]
            l += expand(sub)*b
            start = None
            i = i + a
        elif start == None:
            l += 1
        i += 1
    print("SUB", s, l)
    return l


print(expand(sa))
