# N개의 수로 이뤄진 수열 A1, A2, ... An
# 수와 수 사이에 끼어넣을 수 있는 N-1개의 연산자 주어짐
# 연산자는 +, -, *, % 으로 구성
# 수와 수 사이에 연산자를 넣어서 수식을 하나 구성할 수 있음(수의 순서는 변경 불가능)

# 5개의 자리에 5개가 들어감
# 2개는 공통
# 5! % 2 = 60개

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
operation = list(map(int, input().split()))

maxValue = -1e9
minValue = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maxValue, minValue
    if depth == n:
        maxValue = max(total, maxValue)
        minValue = min(total, minValue)
        return

    if plus:
        dfs(depth+1, total+num[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-num[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*num[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/num[depth]), plus, minus, multiply, divide-1)

dfs(1, num[0], operation[0], operation[1], operation[2], operation[3])
print(maxValue)
print(minValue)