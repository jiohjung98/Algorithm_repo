# import sys

# input = sys.stdin.read().splitlines()

# n = int(input[0])
# arr = list(map(int, input[1].split())) 
# dp = [1] * (n)

# for i in range(1, n):
#     for j in range(0, i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))

# 방법 2 - BS
from bisect import bisect_left
import sys

input = sys.stdin.read().splitlines()

n = int(input[0])
arr = list(map(int, input[1].split())) 
lis = []

for num in arr:
    idx = bisect_left(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        # 값 갱신
        lis[idx] = num

print(len(lis))
