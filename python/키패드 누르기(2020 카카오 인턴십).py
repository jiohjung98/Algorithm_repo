def solution(numbers, hand):
    arr = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
    start_left_x = 3
    start_left_y = 0
    start_right_x = 3
    start_right_y = 2
    result = []
    for n in numbers:
        for i in range(4):
            if n in arr[i]:
                x = arr.index(arr[i])
                y = arr[i].index(n)
                break

        if n == 1 or n == 4 or n == 7:
            result.append('L')
            start_left_x = x
            start_left_y = y
        elif n == 3 or n == 6 or n == 9:
            result.append('R')
            start_right_x = x
            start_right_y = y
        else:
            if abs(start_left_x - x) + abs(start_left_y - y) < abs(start_right_x - x) + abs(start_right_y - y):
                result.append('L')
                start_left_x = x
                start_left_y = y
            elif abs(start_left_x - x) + abs(start_left_y - y) > abs(start_right_x - x) + abs(start_right_y - y):
                result.append('R')
                start_right_x = x
                start_right_y = y
            else:
                if hand == 'left':
                    result.append('L')
                    start_left_x = x
                    start_left_y = y
                else:
                    result.append('R')
                    start_right_x = x
                    start_right_y = y      
    return ''.join(result)