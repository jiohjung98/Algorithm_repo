# 도영이 앞에 n개의 재료
# 각 재료의 신맛 s, 쓴맛 b를 알고있음
# 여러 재료를 이용해서 요리
# -> 신맛 : 신맛의 곱
# -> 쓴맛 : 쓴맛의 합
# 재료를 적절히 섞어서 신맛과 쓴맛의 차이를 가장 적게해야 함

# 예제
# n = 1
# s = 3, b = 10

# 예제 2
# n = 2
# s = 3, b = 8
# s = 5, b = 8

# 재료 1개 사용 -> 3x1=3, 8 => 5
# 재료 2개 사용 -> 3x5=15, 8x2=16 => 1

from itertools import combinations
import math
import sys
input = sys.stdin.readline

n = int(input())
sour = []
bit = [] 
for _ in range(n):
    s, b = tuple(map(int, input().split()))
    sour.append(s)
    bit.append(b)

ans = sys.maxsize

for i in range(1,n+1):
    s_list = combinations(sour, i)
    b_list = combinations(bit, i)
    sb_list = zip(s_list, b_list)
    for elem in sb_list:
        ans = min(ans, abs(math.prod(elem[0]) - sum(elem[1])))

print(ans)