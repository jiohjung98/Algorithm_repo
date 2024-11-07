import sys
sys.stdin = open("input1.txt", "r")

for tc in range(1,11):
    arr_leng = int(input())
    arr = list(map(int, input().split()))

    command_leng = int(input())
    command_input = list(map(str, input().split()))

    command_arr = []
    stack = []
    find_last_idx = 0

    for elem in command_input:
        find_last_idx += 1
        if len(stack) == 0:
            stack.append(elem)
        elif find_last_idx == len(command_input):
            stack.append(elem)
            command_arr.append(stack)
        else:   
            if elem == 'I' or elem == 'D' or elem == 'A':
                command_arr.append(stack)
                stack = []
                stack.append(elem)
            else:
                stack.append(elem)
    

    for i in range(len(command_arr)):
        flag = command_arr[i][0]
        if flag == 'I':
            start_idx = int(command_arr[i][1])
            int_arr = command_arr[i][3:]
            int_arr2 = []
            for j in int_arr:
                int_arr2.append(int(j))
            arr[start_idx:start_idx] = int_arr2                
        elif flag == 'D':
            start_idx = int(command_arr[i][1])
            end_idx = start_idx + int(command_arr[i][2])
            del arr[start_idx:end_idx]
        else:
            int_arr3 = command_arr[i][2:]
            int_arr4 = []
            for j in int_arr3:
                int_arr4.append(int(j))
            arr.append(int_arr4)
    
    ans_arr = arr[:10]
    answer = ' '.join(map(str, ans_arr))

    print(f'#{tc} {answer}')
