# a와 b가 연결, b와 c가 연결 -> a와 c는 간접적으로 연결 -> 정보 교환 가능
# 컴퓨터 개수 n, 연결 정보 2차원 배열 computers -> 네트워크 개수 return

def solution(n, computers):             
    visited = [False] * (n)
    
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if not visited[i] and computers[v][i] == 1:
                dfs(i)
                
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    
    return answer
