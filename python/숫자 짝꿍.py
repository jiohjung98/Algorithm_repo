# 첫 번째 풀이: 시간초과
# def solution(X, Y):
#     answer = ''
#     same_arr = []
#     x_arr = [x for x in X]
#     y_arr = [y for y in Y]
#     for z in x_arr:
#         if z in y_arr:
#             same_arr.append(z)
#             y_arr.remove(z)
#     same_arr.sort(reverse=True)
    
#     if same_arr == []:
#         return '-1'
#     elif same_arr[0] == '0':
#         return '0'
#     else:
#         return ''.join(same_arr)

def solution(X, Y):
    answer = []
    for i in (set(X) & set(Y)):
        for j in range(min(X.count(i), Y.count(i))):
            answer.append(i)
    answer.sort(reverse=True)
    if answer == []:
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        return ''.join(answer)