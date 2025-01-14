# 시간초과
# def solution(N, stages):
#     arr1 = []
#     stages.sort()
#     for i in range(N):
#         clear = 0
#         fail = 0
#         for j in range(i, len(stages)):
#             if stages[j] > i+1:
#                 clear += 1
#             if stages[j] >= i+1 and stages[j] <= i+1:
#                 fail += 1
#         arr1.append(fail/(fail+clear))
    
#     arr2 = sorted(arr1, reverse=True)
#     answer = []
    
#     for elem in arr2:
#         answer.append(arr1.index(elem)+1)
#         arr1[arr1.index(elem)] = 'checked'
    
#     return answer

def solution(N, stages):
    stage_count = [0] * (N+2)
    
    for stage in stages:
        stage_count[stage] += 1
    
    total_user = len(stages)
    stage_fail_rates = []
    for i in range(1, N+1):
        if total_user > 0:
            fail = stage_count[i]
            fail_rate = fail / total_user
            total_user -= fail
        else:
            fail_rate = 0
        stage_fail_rates.append((i, fail_rate))
        
    stage_fail_rates.sort(key=lambda x: (-x[1], x[0]))
    
    answer = [i[0] for i in stage_fail_rates]
    
    return answer
        
    
    
    
    
    
    
    
    
    
    
    
    
    