def solution(food):
    arr = []
    for i in range(1,len(food)):
        cnt = food[i] // 2
        arr.append(str(i) * cnt)
    converted_arr = sorted(arr, reverse=True)

    return ''.join(arr) + '0' + ''.join(converted_arr)