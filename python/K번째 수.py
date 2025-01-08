def solution(array, commands):
    answer =[]
    for i in range(len(commands)):
        i,j,k = commands[i][0], commands[i][1], commands[i][2]
        new_arr = sorted(array[i-1:j])
        answer.append(new_arr[k-1])
    return answer