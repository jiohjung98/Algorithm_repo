import sys
input = sys.stdin.read().splitlines()

w, n = map(int, input[0].split(' '))
arr = []
for i in range(1, n+1):
    a = list(map(int, input[i].split()))
    arr.append(a)

# 금액 높은 순으로 정렬
arr.sort(lambda x: -x[1])

cur_weight = w
ans = 0
while cur_weight > 0:
    for i in range(len(arr)):
        if arr[i][0] <= cur_weight:
            ans += arr[i][0] * arr[i][1]
            cur_weight -= arr[i][0]
        else:
            ans += cur_weight * arr[i][1]
            cur_weight = 0

print(ans)