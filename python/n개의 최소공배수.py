from fractions import gcd

def solution(arr):
    answer = arr[0]
    for elem in arr[1:]:
        answer = (elem * answer) / gcd(elem, answer)
    
    return answer