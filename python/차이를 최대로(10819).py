# n개의 정수로 이뤄진 배열 A
# 배열에 들어있는 정수 순서 적절히 바꿔서 최대값 구하기
# 정해진 식
# | A[0] - A[1] | + | A[1] - A[2] | + ... + | A[n-2] - A[n-1]

# 3
# 1 2 3 5

# 1 2 3 5 -> 1 + 1 + 2 = 4
# 1 2 5 3 -> 1 + 3 + 2 = 6
# 1 3 2 5 -> 2 + 1 + 3 = 6
# 1 3 5 2
# ...

# 풀이 1 (순열)
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cases = list(permutations(arr))

answer = -sys.maxsize

for case in cases:
    middle_ans = 0
    for i in range(n-1):
        middle_ans += abs(case[i] - case[i+1])
    answer = max(answer, middle_ans)

print(answer)