import sys
input = sys.stdin.readline

# 재귀활용법
# 카드를 뽑고 리스트에 저장
# 개수 + 1
# 만약 

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

card_list = []
visited = [False for _ in range(n)]

result = []

def backtracking():
    if len(card_list) == k:
        if ''.join(map(str, card_list)) not in result:
            result.append(''.join(map(str, card_list)))
        return
    
    for i in range(len(arr)):
        if not visited[i]:
            # 방문 처리
            visited[i] = True
            card_list.append(arr[i])
            backtracking()
            card_list.pop()
            visited[i] = False

backtracking()

print(len(result))