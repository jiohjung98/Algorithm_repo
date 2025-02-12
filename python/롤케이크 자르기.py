# 답 맞으나, 시간초과
# def solution(topping):
#     answer = 0
#     for i in range(1, len(topping)-1):
#         front_cake = set(topping[:i])
#         back_cake = set(topping[i:])
#         if len(front_cake) == len(back_cake):
#             answer += 1
#     return answer

from collections import Counter

def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)
    
    for t in topping:
        left.add(t)
        right[t] -= 1
        
        if right[t] == 0:
            del right[t]
        
        if len(left) == len(right):
            answer += 1
    return answer