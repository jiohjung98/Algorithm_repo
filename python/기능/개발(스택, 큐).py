# 방법 1
# import math

# def solution(progresses, speeds):
#     Q= []
#     for p, s in zip(progresses, speeds):
#         if len(Q) == 0 or Q[-1][0] < math.ceil((100-p)/s):
#             Q.append([math.ceil((100-p)/s), 1])
#         else:
#             Q[-1][1] += 1
#     return [q[1] for q in Q]
    
    
# 방법 2
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer