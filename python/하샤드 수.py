def solution(x):
    y = list((str(x)))
    list1 = []
    for d in y:
        list1.append(int(d))
    if (x % sum(list1) == 0):
        answer = True
    else:
        answer = False
    return answer