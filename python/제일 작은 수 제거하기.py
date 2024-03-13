def solution(arr):
    answer = []
    if (len(arr) > 1):
        arr.remove(min(arr))
        return arr
    else:
        return [-1]