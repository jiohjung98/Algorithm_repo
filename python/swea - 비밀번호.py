for tc in range(1, 11):
    n, m = input().split()
    arr = list(m)
    stack = []
    
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    
    for elem in stack:
        elem = int(elem)
    ans = ''.join(stack)

    print(f'#{tc} {ans}')

    # print(f'{tc}',' ',*stack, sep='')

   
for tc in range(1, 11):
    n, m  = input().split()
    stack = []
    m = list(m)
    for a in arr:
        if len(stack) == 0:
            stack.append(a)
        else:
            if stack[-1] == a:
                stack.pop()
            else:
                stack.append(a)
    for elem in stack:
        elem = int(elem)
    ans = ''.join(stack)

    print(f'#{tc} {ans}')