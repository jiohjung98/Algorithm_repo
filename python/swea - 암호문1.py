for tc in range(1,2):
    arr_leng = int(input())
    arr = list(map(int, input().split()))

    command_leng = int(input())
    commad_arr = input().split()

    new_arr = []
    stack = []
    for c in commad_arr:
        if len(stack) == 0:
            stack.append(c)
        else:
            if c == 'I':
                new_arr.append(stack)
                stack = []
                stack.append(c)
            elif commad_arr.index(c) == len(commad_arr) - 1:
                stack.append(c)
                new_arr.append(stack)
                stack = []
            else:
                stack.append(c)

    for i in range(len(new_arr)):
        start_idx = int(new_arr[i][1])
        repeat_cnt = int(new_arr[i][2])
        add_arr = new_arr[i][3:]

        for elem in add_arr[::-1]:
            elem = int(elem)
            arr.insert(start_idx, elem)
    
    ans_arr = arr[:10]
    
    print(f'#{tc}', *ans_arr)
