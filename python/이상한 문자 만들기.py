def solution(s):
    arr = [
        [] for _ in range(len(s.split(' ')))
    ]
    answer = s.split(' ')
    for idx1, a in enumerate(answer):
        for idx2, elem in enumerate(a):
            if idx2 % 2 == 0:
                arr[idx1].append(elem.upper())
            else:
                arr[idx1].append(elem.lower())

    answer = ''
    for idx, x in enumerate(arr):
        if idx > 0:
            answer += ' '
        answer += ''.join(x)
    
    return answer