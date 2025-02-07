# 방법 1 - dp

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0] * n

# for i in range(1, n):
#     for j in range(0, i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i], dp[j]+1)

# print(max(dp)+1)


# 방법 2 - BS(Binary Search)

from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
lis = []

for num in arr:
    idx = bisect_left(lis, num) # num이 들어갈 위치 찾기
    if idx == len(lis):
        lis.append(idx)
    else:
        lis[idx] = num

print(len(lis))

