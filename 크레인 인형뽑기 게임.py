def solution(board, moves):
    # 1 입력 -> board[3][0] = 4
    # 5 입력 -> board[1][4] = 3
    # 3 입력 -> board[1][2] = 1
    # 5 입력 -> board[2][4] = 1
    # 1,1 같으므로 제거 -> +2
    # 1 입력 -> board[4][0] = 3
    # 3, 3 같으므로 제거 -> +2
    # 2 입력 -> board[2][1] = 2
    # 1 입력 -> board[4][0] = x
    # 4 입력 -> board[3][3] = 4
    
    answer = 0
    stack_list = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stack_list.append(board[j][i-1])
                board[j][i-1] = 0
                
                if (len(stack_list) >= 2):
                    if stack_list[-1] == stack_list[-2]:
                        stack_list.pop(-1)
                        stack_list.pop(-1)
                        answer += 2
                break
    return answer