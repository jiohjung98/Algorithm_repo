T = int(input())

for i in range(1, T+1):
    N = int(input())
    ans_arr = []
    for j in range(1, N+1):
        ans_arr.append([])
        for k in range(j):
            if k == 0 or k == j-1:
                ans_arr[j-1].append(1)
            else:
                ans_arr[j-1].append(ans_arr[j-2][k-1] + ans_arr[j-2][k])
    print('#'+str(i))

for ans in ans_arr:
    print(*(ans), end=' ')
    print()