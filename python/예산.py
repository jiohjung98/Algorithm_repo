# def solution(d, budget):
#     tmp = 0
#     answer = 0
#     d.sort()
    
#     for i in range(len(d)):
#         tmp += d[i]
#         if tmp > budget:
#             break
#         else:
#             answer += 1
    
#     return answer

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)