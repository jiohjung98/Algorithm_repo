import re

def solution(dartResult):
    arr = [0]
    divide_by_num_arr = re.findall(r'\d+[A-Z*#]+', dartResult);
    for elem in divide_by_num_arr:
        if len(elem) == 3:
            if elem[2] == '*':
                arr[-1] *= 2
                if elem[1] == 'S':
                    arr.append(int(elem[0]) * 2)
                elif elem[1] == 'D':
                    arr.append((int(elem[0]) **2) * 2)
                else:
                    arr.append((int(elem[0]) ** 3) * 2)
                    continue
            elif elem[2] == '#':
                if elem[1] == 'S':
                    arr.append(int(elem[0]) - int(elem[0]) * 2)
                elif elem[1] == 'D':
                    arr.append(int(elem[0]) ** 2 - (int(elem[0]) ** 2) * 2)
                else:
                    arr.append(int(elem[0]) ** 3 - (int(elem[0]) ** 3) * 2)
            else:
                if elem[2] == 'S':
                    arr.append(int(elem[0:2]))
                elif elem[2] == 'D':
                    arr.append(int(elem[0:2]) ** 2)
                else:
                    arr.append(int(elem[0:2]) ** 3)
        else:
            if elem[1] == 'S':
                arr.append(int(elem[0]))
            elif elem[1] == 'D':
                arr.append(int(elem[0]) ** 2)
            else:
                arr.append(int(elem[0]) ** 3)
    return sum(arr)

# S = 1제곱
# D = 2제곱
# T = 3제곱

# 옵션
# * = 해당 점수와 바로 전 점수 2배
# # = 해당 점수 마이너스
