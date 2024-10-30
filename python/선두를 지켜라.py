n, m = tuple(map(int, input().split()))

a_arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

b_arr = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

a_distance = []
a_cnt = 0

for a in a_arr:
    x, y = a
    while y > 0:
        a_cnt += x
        a_distance.append(a_cnt)
        y -= 1

b_distance = []
b_cnt = 0

for b in b_arr:
    x, y = b
    while y > 0:
        b_cnt += x
        b_distance.append(b_cnt)
        y -= 1

ans = 0
flag = '0'

for i in range(len(b_distance)):
    if a_distance[i] == b_distance[i]:
        continue
    elif a_distance[i] > b_distance[i]:
        if flag == 'a':
            continue
        else:
            ans += 1
            flag = 'a'
    else:
        if flag == 'b':
            continue
        else:
            ans += 1
            flag = 'b'

print(ans)