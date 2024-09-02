def solution(my_string):
    n = my_string.split()
    x = [y for y in n if y.isdigit()]
    y = [x for x in n if x.isdigit() == False]
    answer = x[0]
    for i in range(len(y)):
        if y[i] == '+':
            answer += int(x[i+1])
        else:
            answer -= int(x[i+1])
    return answer


my_string ="3 + 4 - 7 + 5"

solution(my_string)