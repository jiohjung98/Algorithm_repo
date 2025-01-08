def solution(a, b, n):
    answer = 0
    while n >= a:
        new_bottles = (n // a) * b
        remain_bottles = n % a
        answer += new_bottles
        n = new_bottles + remain_bottles
    return answer