def solution(k, m, score):
    answer = 0
    arr = []
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        arr.append(score[i:i+m])
    for j in range(len(arr)):
        if len(arr[j]) == m:
            answer += min(arr[j]) * m
    return answer