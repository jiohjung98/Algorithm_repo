def solution(strArr):
    ans = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            ans.append(strArr[i].lower())
        else:
            ans.append(strArr[i].upper())
    return ans