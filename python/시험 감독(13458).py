# 총 N개의 시험장
# i번 시험장에 있는 응시자의 수 : Ai명
# 감독관 : 총감독관, 부감독관
# 총감독관 : 감시 응시자 수 B명
# 부감독관 : 감시 응시자 수 C명
# 총감독관은 1명, 부감독관은 1명 이상 가능
# 필요한 감독관 수의 최솟값 구하기

# 입력
# line 1 : 시험장 개수 N
# line 2 : 각 시험장에 있는 응시자 수 Ai
# line 3 : B, C

# ex)
# 3
# 3 4 5
# 2 2
# 시험장 개수 3개
# 1시험장: 3명, 2시험장: 4명, 3시험장: 5명
# 총감독관이 감시할 수 있는 응시자 수 : 2명, 부감독관이 감시할 수 있는 응시자 수 : 2명
# 1시험장에 총감독관 1명, 부감독관 1명
# 2시험장에 총감독관 1명, 부감독관 1명
# 3시험장에 총감독관 1명, 부감독관 2명
import math
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
b, c = tuple(map(int, input().split()))

new_arr = []
total = 0
for elem in arr:
    if elem < b:
        new_arr.append(0)
    else:
        new_arr.append(elem-b)

for elem in new_arr:
    total += math.ceil(elem / c)

total += len(new_arr)
print(total)