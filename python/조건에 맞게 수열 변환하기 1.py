def solution(arr):
    ans = []
    for elem in arr:
        if elem >= 50 and elem % 2 == 0:
            ans.append(elem//2)
        elif elem < 50 and elem % 2 != 0:
            ans.append(elem*2)
        else:
            ans.append(elem)
    return ans