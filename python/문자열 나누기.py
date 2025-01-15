# 시간초과
# def solution(s):
#     s = list(s)
#     cnt = 0
#     while len(s) > 1:
#         first_char = s[0]
#         first_char_cnt = 1
#         diff_char_cnt = 0
#         for i in range(1, len(s)):
#             if s[i] != first_char:
#                 diff_char_cnt += 1
#             if s[i] == first_char:
#                 first_char_cnt += 1
#             if diff_char_cnt == first_char_cnt:
#                 s = s[i+1:]
#                 cnt += 1
#                 break
#     if len(s) == 0:
#         return cnt
#     else:
#         return cnt + 1

def solution(s):
    answer = 0
    cnt1 = 0
    cnt2 = 0
    for i in s:
        if cnt1 == cnt2:
            answer += 1
            k= i
        if k == i:
            cnt1 += 1
        else:
            cnt2 += 1
    return answer