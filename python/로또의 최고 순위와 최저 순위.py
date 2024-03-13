def solution(lottos, win_nums):
    answer = []
    zero_sum = lottos.count(0)
    cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
            
    max_value = min(6, 7-(cnt+zero_sum))
    min_value = min(6, 7-cnt)
    answer.append(max_value)
    answer.append(min_value)

    return answer