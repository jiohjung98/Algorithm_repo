# bfs
def solution(numbers, target):
    leaves = [0]
    for number in numbers:
        tmp = []
        for leaf in leaves:
            tmp.append(leaf + number)
            tmp.append(leaf - number)
        leaves = tmp
    answer = leaves.count(target)
    return answer

# dfs
answer = 0

def dfs(numbers, target, current, index):
    global answer
    if len(numbers) == index:
        if current == target:
            answer += 1
        return
    
    dfs(numbers, target, current + numbers[index], index + 1)
    dfs(numbers, target, current - numbers[index], index + 1)


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer 