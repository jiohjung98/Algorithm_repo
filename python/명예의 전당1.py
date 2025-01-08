def solution(k, score):
    stack = []
    answer = []
    for i in range(len(score)):
        stack.append(score[i])
        stack.sort(reverse=True)
        if len(stack) == k+1:
            stack.pop()
        answer.append(stack[-1])
    return answer