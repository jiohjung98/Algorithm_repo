# def solution(number, limit, power):
#     arr = [
#         i for i in range(1, number+1)
#     ]
#     arr2 = []
#     for a in arr:
#         cnt = 0
#         for i in range(1,int(a**0.5)+1):
#             if i * i == a:
#                 cnt += 1
#                 continue
#             if a % i == 0:
#                 cnt += 2
#         arr2.append(cnt)
#     answer =[]
#     for b in arr2:
#         if b <= limit:
#             answer.append(b)
#         else:
#             answer.append(power)
#     return sum(answer)

def solution(number, limit, power):
    # 약수 개수 배열
    arr = [0] * (number+1)
    
    # 효율적인 약수 계산
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            arr[j] += 1
    
    answer = 0
    for elem in arr[1:]:
        if elem <= limit:
            answer += elem
        else:
            answer += power
            
    return answer