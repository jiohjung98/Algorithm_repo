def solution(n, words): 
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            if (i+1) % n == 0:
                return [n, (i+1)//n]
            else:
                return [(i+1) % n, (i+1) // n + 1]
    else:
        return [0, 0]