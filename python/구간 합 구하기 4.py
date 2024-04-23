# 백준 11659번

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
nums = list(map(int, input().split()))
sum_list = [0]
temp = 0

for i in nums:
    temp += i
    sum_list.append(temp)

for i in range(y):
    a, b = map(int, input().split())
    print(sum_list[b] - sum_list[a-1])