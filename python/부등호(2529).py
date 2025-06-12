# A = 두 종류의 부등호 '<', '>' 가 k개 나열
# 부등호 기호 앞뒤에 서로 다른 한자리 숫자를 넣어서 모든 관계 만족시키고자 함

import sys
input = sys.stdin.readline

def checkNums(front, back, operation):
    if operation == '<':
        if front > back:
            return False
    if operation == '>':
        if front < back:
            return False
    return True

def dfs(cnt, nums):
    if cnt == k+1:
        answer_list.append(nums)
        return
    
    for i in range(10):
        if visited[i]:
            continue
        if cnt == 0 or checkNums(int(nums[-1]), i, arr[cnt-1]):
            visited[i] = True
            dfs(cnt+1, nums+str(i))
            visited[i] = False

k = int(input())
arr = list(map(str, input().split()))
answer_list = []
visited = [0] * 10

dfs(0, '')
answer_list.sort()
print(answer_list[-1])
print(answer_list[0])


