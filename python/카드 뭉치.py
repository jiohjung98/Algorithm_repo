# 기존 풀이 - 리스트, pop() 사용 -> 리스트 크기가 커지면 효율성 낮아짐(O(n))

# def solution(cards1, cards2, goal):
#     for i in range(len(goal)):
#         if len(cards1) > 0 and goal[i] == cards1[0]:
#             cards1.pop(0)
#         elif len(cards2) > 0 and goal[i] == cards2[0]:
#             cards2.pop(0)
#         else:
#             return 'No'
#     return 'Yes'


# deque 사용 -> 양뱡향 큐로 설정되어있어서 효율적(O(1))
from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for i in range(len(goal)):
        if len(cards1) > 0 and goal[i] == cards1[0]:
            cards1.popleft()
        elif len(cards2) > 0 and goal[i] == cards2[0]:
            cards2.popleft()
        else:
            return 'No'
    return 'Yes'