# 카드 5장
# 숫자 : 1, 2, 3, 13, 21
# 3장 선택
# 2 1 13 -> 2113
# 21 1 3 -> 2113
# 한 정수를 만드는 조합이 여러가지일 수 있음

# ex) n = 4, k = 2
# 1, 2, 12, 1
# 1 1
# 1 2
# 2 1
# 1 12
# 12 1
# 12 2
# 2 12

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

comb_arr = permutations(arr, k)

result = []
for elem in comb_arr:
    x = ''.join(map(str, elem))
    result.append(x)

result = list(set(result))
print(len(result))