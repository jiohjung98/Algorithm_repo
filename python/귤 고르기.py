# def solution(k, tangerine):
#     total_count = len(tangerine)
#     target_arr = []
#     answer = 0
#     for t in set(tangerine):
#         target_count = tangerine.count(t)
#         target_arr.append(target_count)
#     if max(target_arr) >= k:
#         answer = 1
#     else:
#         target_arr.sort(reverse=True)
#         tmp = 0
#         for t in target_arr:
#             tmp += t
#             answer += 1
#             if tmp >= k:
#                 break
#     return answer

def solution(k, tangerine):
    count_dict = {}
    for t in tangerine:
        count_dict[t] = count_dict.get(t, 0) + 1

    target_arr = sorted(count_dict.values(), reverse=True)
    answer = 0
    tmp = 0
    for count in target_arr:
        tmp += count
        answer += 1
        if tmp >= k:
            break
    return 1 if max(target_arr) >= k else answer

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]	

solution(k, tangerine)