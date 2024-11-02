n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

ans_arr = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            arr[i], arr[j], arr[k] = str(arr[i]), str(arr[j]), str(arr[k])
            max_len = max(len(arr[i]),len(arr[j]),len(arr[k]))
            arr[i] = '0' * (max_len - len(arr[i])) + arr[i]
            arr[j] = '0' * (max_len - len(arr[j])) + arr[j]
            arr[k] = '0' * (max_len - len(arr[k])) + arr[k]
            tmp_arr = []
            for l in range(max_len):
                if int(arr[i][l]) + int(arr[j][l]) + int(arr[k][l]) < 10:
                    tmp_arr.append(str(int(arr[i][l]) + int(arr[j][l]) + int(arr[k][l])))
                else:
                    tmp_arr = []
                    break
            if tmp_arr != []:
                tmp_num = ''.join((tmp_arr))
                tmp_num = int(tmp_num)
                ans_arr.append(tmp_num)

if ans_arr == []:
    print(-1)
else:
    print(max(ans_arr))



                
