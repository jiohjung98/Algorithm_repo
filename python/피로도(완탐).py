from itertools import permutations

def solution(k, dungeons):
    arr = list(permutations(dungeons, len(dungeons)))
    max_cnt = 0
    
    for elem in arr:
        cnt = 0
        remain_k = k
        for required, consumption in elem:
            if remain_k >= required:
                cnt += 1
                remain_k -= consumption
                if cnt == len(dungeons):
                    return max_cnt
            else:
                break
        max_cnt = max(max_cnt, cnt)
            
    return max_cnt

solution(80, [[80,20],[50,40],[30,10]])