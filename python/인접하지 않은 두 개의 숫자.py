n = int(input())
arr = list(map(int,input().split()))

sum_arr = []
for i in range(n):
    for j in range(n):
        if i != j and i-1 != j and i != j-1:
            sum_arr.append(arr[i] + arr[j])

print(max(sum_arr))