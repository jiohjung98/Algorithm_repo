import sys
input = sys.stdin.readline


s = input()
word_stack = []
tag = False
res = ''

for x in s:
    if x == ' ':
        while word_stack:
            res += word_stack.pop()
        res += x
    
    elif x == '<':
        while word_stack:
            res += word_stack.pop()
        tag = True
        res += x

    elif x == '>':
        tag = False
        res += x
    
    elif tag:
        res += x

    else:
        word_stack.append(x)

while word_stack:
    res += word_stack.pop()
print(res)