import sys
input = sys.stdin.readline().split()
arr = list(map(int, input))

# if arr[0] == 1:
#     for i in range(1, len(arr)):
#         if arr[i-1] < arr[i]:
#             continue
#         else:
#             print('mixed')
#             exit(0)
#     print('ascending')

# elif arr[0] == 8:
#     for i in range(1, len(arr)):
#         if arr[i-1] > arr[i]:
#             continue
#         else:
#             print('mixed')
#             exit(0)
#     print('descending')

# else:
#     print('descending')

if arr == sorted(arr):
    print("ascending")
elif arr == sorted(arr, reverse=True):
    print("descending")
else:
    print("mixed")