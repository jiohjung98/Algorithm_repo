N, M = map(int, input().split())
graph = []
house = []
chicken = []

for col in range(N):
    graph.append(list(map(int, input().split())))
    for row in range(N):
        if graph[col][row] == 1:
            house.append((col, row))
        elif graph[col][row] == 2:
            chicken.append((col, row))

arr = []
real_check = int(1e9)

def back_traking(num, cnt):
    global real_check

    if num > len(chicken):
        return

    if cnt == M:
        result_val = 0
        for hx, hy in house:
            min_check = int(1e9)

            for idx in arr:
                cx, cy = chicken[idx]
                min_check = min(min_check, abs(hx-cx) + abs(hy-cy))
            
            result_val += min_check
        
        real_check = min(real_check, result_val)
        return
    
    arr.append(num)
    back_traking(num+1, cnt+1)
    arr.pop()
    back_traking(num+1, cnt)
    return real_check

back_traking(0,0)
print(real_check)