import collections

file_content = open('ex', 'r').readlines()
s = file_content[0]

res = ""
i = 0
start = None
while i < len(s):
    c = s[i]
    if c == "(":
        start = i
    elif c == ")":
        a, b = [int(q) for q in s[start+1:i].split('x')]
        print(a, b)
        res += s[i+1:a+i+1]*b
        start = None
        i = i + a
    elif start == None:
        res += c
    i += 1
print(res, len(res))
