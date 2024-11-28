import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    arr_leng = int(input())
    arr = list(map(int, input().split()))

    command_leng = int(input())
    command_input = list(map(str, input().split()))

    stack = []
    command_arr = []
    find_last_char = 0
    for elem in command_input:
        # 마지막 요소인지 확인하기 위해
        find_last_char += 1
        if len(stack) == 0:
            stack.append(elem)
        # elem이 마지막 원소일 때
        elif find_last_char == len(command_input) :
            stack.append(elem)
            command_arr.append(stack)
        else:
            if elem == 'I' or elem == 'D':
                command_arr.append(stack)
                stack = []
                stack.append(elem)
            else:
                stack.append(elem)

    for i in range(len(command_arr)):
        flag = command_arr[i][0]
        cur_arr_leng = len(command_arr[i])
        if flag == 'I':
            add_index = int(command_arr[i][1])
            add_cnt = int(command_arr[i][2])
            int_arr = []
            for elem in command_arr[i][3:]:
                elem = int(elem)
                int_arr.append(elem)
            arr[add_index:add_index] = int_arr
        else:
            delete_index = int(command_arr[i][1])
            delete_cnt = int(command_arr[i][2])
            del arr[delete_index:delete_index+delete_cnt]
    
    ans_arr = arr[:10]
    answer = ' '.join(map(str, ans_arr))

    print(f'#{tc} {answer}')
