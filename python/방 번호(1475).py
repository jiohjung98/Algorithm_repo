from collections import Counter

n =list(input())
arr = Counter(n)

arr['9'] += arr['6']
del arr['6']

if arr['9'] % 2 == 0:
    arr['9'] //= 2
else:
    arr['9'] //= 2
    arr['9'] += 1

max_key = max(arr, key=arr.get)
max_value = arr[max_key]

print(max_value)