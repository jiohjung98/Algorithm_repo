from itertools import combinations

def solution(number):
    arr = list(combinations(number,3))
    cnt = 0
    for elem in arr:
        if sum(elem) == 0:
            cnt += 1
    return cnt