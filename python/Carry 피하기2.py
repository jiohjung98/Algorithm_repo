n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
max_len = 0
for elem in arr:
    max_len = max(max_len, len(str(elem)))

new_arr = []
for elem in arr:
    elem = '0' * (max_len - len(str(elem))) + str(elem)
    new_arr.append(elem)

ans_arr = []       
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = '0'
            cnt = 0
            for l in range(max_len):
                if int(new_arr[i][l]) + int(new_arr[j][l]) + int(new_arr[k][l]) < 10:
                    tmp += str(int(new_arr[i][l]) + int(new_arr[j][l]) + int(new_arr[k][l]))
                    cnt += 1
            if cnt == max_len:
                ans_arr.append(tmp)

ans = 0
for elem in ans_arr:
    if int(elem) > ans:
        ans = int(elem)

if ans == 0:
    print(-1)
else:
    print(ans)