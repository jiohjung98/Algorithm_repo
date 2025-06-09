# 수빈이가 가장 관심있어하는 소수 : 7331
# 7331 : 소수, 733: 소수, 73: 소수, 7 : 소수
# 신기한 소수 : 왼쪽부터 셌을 때 그 수가 다 소수인 수

# 풀이 방법
# 소수 판별 알고리즘 필요(is_prime)
# 한 자리 소수(2, 3, 5, 7)에 10씩 곱하고 0~9를 더했을 때 소수인지 판별

import sys
input = sys.stdin.readline

n = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if is_prime(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)