def solution(babbling):
    cnt = 0
    for i in babbling:
        for j in ["aya", "ye", "woo", "ma"]:
            if 2*j not in i:
                i = i.replace(j, ' ')
        if len(i.strip()) == 0:
            cnt += 1
    return cnt