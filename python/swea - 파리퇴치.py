T = int(input())

for i in range(1, T+1):
    N, M = tuple(map(int, input().split()))
    arr = []
    for j in range(N):
        a = list(map(int, input().split()))
        arr.append(a)
    sum_arr = []
    for x in range(N-M+1):
        for y in range(N-M+1):
            sum_of_arr = 0
            for z in range(M):
                for w in range(M):
                    sum_of_arr += arr[x+z][y+w]
            sum_arr.append(sum_of_arr)
    print('#'+str(i), max(sum_arr))
            