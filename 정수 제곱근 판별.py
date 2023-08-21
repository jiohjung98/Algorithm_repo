# // 시간초과 코드
# def solution(n):
#     answer = 0
#     for i in range(1, n):
#         if (i*i == n):
#             answer = (i+1)*(i+1)
#             break
#         else:
#             answer = -1
#     return answer

def solution(n):
    answer = 0
    for i in range(1, n):
        if (i*i == n):
            answer = (i+1)*(i+1)
            break
        else:
            answer = -1
    return answer