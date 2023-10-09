def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt = 0
        for x in target:
            flag = False    
            max_len = 101    
            for key in keymap:
                if x in key:
                    max_len = min(key.index(x)+1, max_len)
                    flag = True
            if not flag:
                cnt = -1
                break
            cnt += max_len
        answer.append(cnt)
    return answer