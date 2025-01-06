def solution(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    arr = []
    for elem in s:
        if elem == ' ':
            arr.append(' ')
        elif elem.islower() is True:
            append_idx = lower_list.find(elem) + n
            arr.append(lower_list[append_idx % 26])
        else:
            append_idx = upper_list.find(elem) + n
            arr.append(upper_list[append_idx % 26])
                
    return ''.join(arr)