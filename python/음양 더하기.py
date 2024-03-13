def solution(absolutes, signs):
    answer = []
    for i in range(0, len(signs)):
        if signs[i] == True:
            answer.append(absolutes[i])
        else:
            answer.append(absolutes[i]-2*absolutes[i])
    return sum(answer)