# 시간 초과
# def solution(s, skip, index):
#     answer = ''
#     alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
#     for elem in s:
#         idx = alphabets.index(elem)
#         arr1 = alphabets[idx+1: idx+1+index]
#         plus_cnt = 0
#         for a in skip:
#             if a in arr1:
#                 plus_cnt += 1
#                 arr1.remove(a)
#         arr1 += (alphabets[(idx+1+index)%26:(idx+1+index+plus_cnt) % 26])
#         answer += arr1[-1]
#     return answer

def solution(s, skip, index):
    answer = ''
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for alphabet in skip:
        alphabets.remove(alphabet)
    for char in s:
        new_index = alphabets.index(char) + index
        answer += alphabets[new_index % len(alphabets)]
    return answer