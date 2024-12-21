from itertools import combinations

n, s = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

comb = list(combinations(arr, n-2))
new_arr = []
for elem in comb:
    new_arr.append(sum(elem))

ans_arr = []
for elem in new_arr:
    ans_arr.append(abs(elem-s))

print(min(ans_arr))