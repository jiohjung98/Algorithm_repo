# for tc in range(1,11):
#     arr_leng = int(input())
#     arr = list(map(int, input().split()))

#     command_leng = int(input())
#     commad_arr = input().split()

#     new_arr = []
#     stack = []
#     for c in commad_arr:
#         if len(stack) == 0:
#             stack.append(c)
#         else:
#             if c == 'I':
#                 new_arr.append(stack)
#                 stack = []
#                 stack.append(c)
#             elif commad_arr.index(c) == len(commad_arr) - 1:
#                 stack.append(c)
#                 new_arr.append(stack)
#                 stack = []
#             else:
#                 stack.append(c)

#     for i in range(len(new_arr)):
#         start_idx = int(new_arr[i][1])
#         repeat_cnt = int(new_arr[i][2])
#         add_arr = new_arr[i][3:]

#         for elem in add_arr[::-1]:
#             elem = int(elem)
#             arr.insert(start_idx, elem)
    
#     ans_arr = arr[:10]
    
#     print(f'#{tc}', *ans_arr)

for tc in range(1,11):
    n = int(input())
    arr = list(map(int, input().split()))

    command_leng = int(input())
    # 첫 번째 요소 'I'를 제거하고 저장
    command = input().split("I")[1:] 

    for i in command:
        # 공백을 기준으로 문자열 새로 저장
        new_command = list(map(int, i.split()))
        start_idx = new_command[0]
        num_to_add_list = new_command[2:]

        # start_idx 자리에 추가할 숫자들 저장
        arr[start_idx:start_idx] = num_to_add_list
    
    ans_arr = arr[:10]
    print(f'{tc} {''.join(map(str, ans_arr))}')
