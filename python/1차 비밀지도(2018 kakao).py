# def solution(n, arr1, arr2):
#     arr = []
#     answer = []
#     for i in range(n):
#         arr1_tmp = bin(arr1[i])[2:]
#         arr2_tmp = bin(arr2[i])[2:]
#         add_cnt1 = n - len(arr1_tmp)
#         add_cnt2 = n - len(arr2_tmp)
#         arr1_tmp = '0' * add_cnt1 + arr1_tmp
#         arr2_tmp = '0' * add_cnt2 + arr2_tmp
#         new_val = ''
#         for j in range(n):
#             if int(arr1_tmp[j]) + int(arr2_tmp[j]) == 0:
#                 new_val += '0'
#             else:
#                 new_val += '1'
#         arr.append(new_val)
#     for elem in arr:
#         val1 = elem.replace('1', '#')
#         val2 = val1.replace('0', ' ')
#         answer.append(val2)
#     return answer


def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        tmp = bin(i | j)[2:]
        tmp = tmp.rjust(n, '0')
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)
    return answer