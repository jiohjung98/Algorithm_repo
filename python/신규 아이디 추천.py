def solution(new_id):
    avaliable_char = ['-', '_', '.']
    answer = ''
    lower_id = list(new_id.lower())
    removed_arr = []
    for i in lower_id:
        if i.isalnum() or i in avaliable_char:
            removed_arr.append(i)
    joined_arr = ''.join(removed_arr)
    while '..' in joined_arr:
        joined_arr = joined_arr.replace('..', '.')
    if joined_arr[0] == '.' and len(joined_arr) > 1:
        joined_arr = joined_arr[1:]
    if joined_arr[-1] == '.':
        joined_arr = joined_arr[:-1]
    if joined_arr == '':
        joined_arr = 'a'
    if len(joined_arr) >= 16:
        joined_arr = joined_arr[:15]
        if joined_arr[-1] == '.':
            joined_arr = joined_arr[:-1]
    if len(joined_arr) <= 2:
       joined_arr = joined_arr + joined_arr[-1] * (3-len(joined_arr))
    return joined_arr

new_id = "...!@BaT#*..y.abcdefghijklm"
solution(new_id)