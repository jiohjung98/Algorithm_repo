from itertools import combinations

def solution(nums):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    
    cnt = 0
    for j in combinations(nums, 3):
        if is_prime(sum(j)):
            cnt += 1
    return cnt