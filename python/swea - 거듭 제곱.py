def func(a,b):
    if a == 0:
        return 1
    else:
        return a * func(a,b-1)
    

for tc in range(1,3):
    n = input()
    a,b = tuple(map(int, input().split()))
    
    result = func(a,b)
    
    print('#'+n, func(a, b))