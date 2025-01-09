def solution(name, yearning, photo):
    arr = []
    for i in range(len(photo)):
        score = 0
        for j in photo[i]:
            if j in name:
                score += yearning[name.index(j)]
        arr.append(score)
    return arr