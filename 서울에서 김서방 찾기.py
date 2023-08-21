def solution(seoul):
    answer = 0 
    for i in range(0, len(seoul)):
        if (seoul[i] == 'Kim'):
            answer = i
    return ('김서방은 ' + str(answer) + '에 있다')