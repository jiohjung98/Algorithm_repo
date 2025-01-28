from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    names = deque()
    for i in range(len(queue)) :
        names.append(chr(ord('A')+i))
    find_char = names[location]
    while find_char in names:
        back = False
        x = queue.popleft()
        y = names.popleft()
        for q in queue:
            if x < q:
                queue.append(x)
                names.append(y)
                back = True
                break
        if back == False:
            answer += 1
    return answer


# 2번 : any 사용 -> 하나라도 true면 실행
def solution(priorities, location):
    queue = [(i,p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer